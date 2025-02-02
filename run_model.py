import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI(title="Qwen2.5-Coder Agent")

model = None
tokenizer = None


@app.post("/load_model")
def load_model():
    global model, tokenizer

    model_name = "Qwen/Qwen2.5-Coder-1.5B"
    print(f"Loading model {model_name}...")

    tokenizer_local = AutoTokenizer.from_pretrained(
        model_name, 
        trust_remote_code=True
    )
    model_local = AutoModelForCausalLM.from_pretrained(
        model_name,
        trust_remote_code=True,
        device_map="auto" 
    )
    model_local.eval()

    tokenizer, model = tokenizer_local, model_local
    print(f"Model {model_name} loaded successfully.")


class GenerateRequest(BaseModel):
    prompt: str
    max_length: Optional[int] = 256
    temperature: Optional[float] = 0.8


@app.post("/generate")
def generate_code(req: GenerateRequest):
    global model, tokenizer

    if model is None or tokenizer is None:
        return {"error": "Model not loaded yet."}

    inputs = tokenizer(req.prompt, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_length=req.max_length,
            do_sample=True,
            temperature=req.temperature
        )

    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"result": generated_text}


if __name__ == "__main__":
    uvicorn.run("run_agent:app", host="0.0.0.0", port=8000, reload=False)
