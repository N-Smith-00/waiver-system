from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""]
)

@app.post("/submit")
async def submit(data: dict):
    print(data)

    # save to database
    # send email confirmation

    return {"success": True}