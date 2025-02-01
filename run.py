from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from leetcode_client import LeetCodeClient
from leetcode_config import LEETCODE_SESSION, CSRF_TOKEN

app = FastAPI(title="LeetCode Submission API")

leetcode_client = LeetCodeClient(
    session_cookie=LEETCODE_SESSION,
    csrf_token=CSRF_TOKEN,
    debug=False  
)

class SubmissionRequest(BaseModel):
    code: str
    problem_slug: str
    question_id: str
    language: Optional[str] = "python3"

class SubmissionResponse(BaseModel):
    status: bool
    details: dict

@app.post("/submit")
async def submit_solution(submission: SubmissionRequest):
    try:
        result = leetcode_client.submit_solution(
            code=submission.code,
            problem_slug=submission.problem_slug,
            question_id=submission.question_id,
            lang=submission.language
        )
        
        return {
            "status": 1 if result.get("status_msg") == "Accepted" else 0,
            "details": result
        }
    except Exception as e:
        print(f"Error details: {str(e)}")  
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)