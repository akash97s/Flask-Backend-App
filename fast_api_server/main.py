from fastapi import FastAPI, Request
from flask import request
# from Helper.logger import setup_logger, log_request

app = FastAPI()
# setup_logger()

@app.get("/", summary = "Home URL example")
# @log_request()
async def home():
    return {"message": "First FastAPI example"}

@app.get("/users/{name}", summary = "URL params example")
async def urlParam(name: str):
    return {"message": f"Hi {name}"}
