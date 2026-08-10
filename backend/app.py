from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, date
from utils import create_confirmation_adult


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
    # add in date signed and expriation date
    data["date_signed"] = datetime.now()
    try:
        data["expiration_date"] = date.today().replace(year=date.today().year + 1)
    except ValueError:
        data["expiration_date"] = date.today().replace(year=date.today().year + 1, month=date.today().month + 1, day=1)

    # adult check
    if (datetime.now() - datetime.fromisoformat(data["dob"])).days/365 <= 18:
        if not "guard_ack" in data:
            return {"success": False, "error": "Participants under 18 must have a parent or guardian fill out the minor waiver"}
        if (datetime.now() - datetime.fromisoformat(data["guard_dob"])).days/365 <= 18:
            return {"success": False, "error": "Guardian must be over the age of 18"}

    # emergency contact check
    if (data["ec_fname"] == data["fname"] and data["ec_lname"] == data["lname"]) or data["ec_phone_num"] == data["phone_num"]:
        return {"success": False, "error": "Emergency contact cannot be yourself"}


    # save to database
    # send email confirmation
    if not "guard_ack" in data:
        create_confirmation_adult(data)
    else:
        pass

    return {"success": True}