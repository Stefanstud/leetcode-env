from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Optional
from leetcode_client import LeetCodeClient
import os

PROBLEMS = []
with open ("data/leetcode_questions_2023_08_08.json", "r") as f:
    entry = f.read() 
    PROBLEMS.append(
        {
            "problem_slug": entry["title_slug"],
            "question_id": entry["question_id"],
            "content": entry["content"],
        }
    )
    
current_index = 0

class Settings(BaseSettings):
    leetcode_session: str = os.getenv("LEETCODE_SESSION")
    csrf_token: str = os.getenv("CSRF_TOKEN")

class SubmissionRequest(BaseModel):
    code: str
    problem_slug: str
    question_id: str
    language: Optional[str] = "python3"
    session_cookie: Optional[str]
    csrf_token: Optional[str]

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
    submission: SubmissionRequest
):
    """Submit solution to LeetCode problem, with tokens passed in the body."""
    try:
        session_cookie = submission.session_cookie or "your_default_session"
        csrf = submission.csrf_token or "your_default_csrf"

        client = LeetCodeClient(
            session_cookie=session_cookie,
            csrf_token=csrf,
            debug=False
        )

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

@app.get("/generate")
def generate_problem():
    """
    Return the next problem from the local list (round-robin).
    Every time this endpoint is called, we move to the next problem in PROBLEMS.
    """
    global current_index
    if not PROBLEMS:
        raise HTTPException(status_code=404, detail="No problems found.")

    problem = PROBLEMS[current_index]
    current_index = (current_index + 1) % len(PROBLEMS)  # cycle through

    return {
        "problem_slug": problem["problem_slug"],
        "question_id": problem["question_id"],
        "task": problem["content"],
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)