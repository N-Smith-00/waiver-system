from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/baseline-waiver-test/submit")
async def submit(data: dict):
    print(data)

    # adult check
    if (datetime.now() - datetime.fromisoformat(data["dob"])).days/365 <= 18 and not "guard-ack" in data:
        return {"success": False, "error": "Participants under 18 must have a parent or guardian fill out the minor waiver"}

    # emergency contact check


    # save to database
    # send email confirmation

    return {"success": True}