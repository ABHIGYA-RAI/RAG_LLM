from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException
app = FastAPI()

@app.post("/documents/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="You can only upload PDF files.😅")
    return {"Filename" : file.filename}