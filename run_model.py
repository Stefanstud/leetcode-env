import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI(title="Qwen2.5-Coder")

model = None
tokenizer = None

def load_model():
    global model, tokenizer

    model_name = "Qwen/Qwen2.5-Coder-0.5B-Instruct"

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

    messages = [
        {
            "role": "system",
            "content": (
                "You are a coding assistant. Please output only valid Python code "
                "without docstrings, extra commentary, or explanations. "
                "Start directly with the code. Do not restate the question."
            )
        },
        {
            "role": "user",
            "content": req.prompt 
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_length=req.max_length or 256,
            do_sample=True,
            temperature=req.temperature or 0.8
        )

    generated_ids = [
        output_ids[len(input_ids):] 
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    if "```python" in generated_text:
        parts = generated_text.split("```python")
        generated_text = parts[1] if len(parts) > 1 else parts[0]  
        generated_text = generated_text.split("```")[0] 
    else:
        generated_text = generated_text.strip()
        lines = generated_text.split("\n")
        while lines and not lines[0].startswith("class"):
            lines.pop(0)

        generated_text = "\n".join(lines) 

    return {"result": generated_text.strip()}

if __name__ == "__main__":
    load_model()
    uvicorn.run(app, host="0.0.0.0", port=8001)