from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

#GET Resource
@app.get("/")
def root_check():
    return {
        "Message" : "API Working Successfully!"
    }

#POST Resource
@app.post("/add")
async def add_numbers(request : Request):
    body = await request.body()
    body = json.loads(body)
    print("The body is: " + body)
    sum = int(body["num1"]) + int(body["num2"])
    return {"sum" : sum, "value_selected": body["radioValue"]}
