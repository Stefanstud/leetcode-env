from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Optional
from leetcode_client import LeetCodeClient
import os

class Settings(BaseSettings):
    leetcode_session: str = os.getenv("LEETCODE_SESSION")
    csrf_token: str = os.getenv("CSRF_TOKEN")

class SubmissionRequest(BaseModel):
    code: str
    problem_slug: str
    question_id: str
    language: Optional[str] = "python3"

app = FastAPI(title="LeetCode Submission API")

def get_leetcode_client():
    settings = Settings()
    return LeetCodeClient(
        session_cookie=settings.leetcode_session,
        csrf_token=settings.csrf_token,
        debug=False
    )

@app.post("/submit")
async def submit_solution(
    submission: SubmissionRequest,
    client: LeetCodeClient = Depends(get_leetcode_client)
):
    """Submit solution to LeetCode problem"""
    try:
        result = client.submit_solution(
            code=submission.code,
            problem_slug=submission.problem_slug,
            question_id=submission.question_id,
            lang=submission.language
        )
        
        return {
            "accepted": result.get("status_msg") == "Accepted",
            "runtime": result.get("status_runtime"),
            "memory": result.get("status_memory"),
            "total_testcases": result.get("total_testcases"),
            "passed_testcases": result.get("total_correct")
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Submission failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)