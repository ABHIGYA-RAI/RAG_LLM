from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

app = FastAPI()
@app.post("/documents/upload")
async def upload(file:UploadFile = File(...)):
    return {"yep, you got the file" : file.filename}

#This code is the API
