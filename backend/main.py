from fastapi import FastAPI, Request, HTTPException
from agents.code_analyzer_agent import analyze_code_diff
from agents.review_monitor_agent import monitor_review
from agents.merge_gatekeeper_agent import check_merge_approval
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GITHUB_SECRET = os.getenv("GITHUB_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")
    if event == "pull_request":
        pr_data = payload.get("pull_request", {})
        # 1. Analyze code diff
        analysis = analyze_code_diff(pr_data)
        # 2. Monitor review
        review_status = monitor_review(pr_data)
        # 3. Gatekeeper for merge
        merge_allowed = check_merge_approval(pr_data, analysis, review_status)
        return {
            "analysis": analysis,
            "review_status": review_status,
            "merge_allowed": merge_allowed
        }
    return {"message": "Event not handled"}