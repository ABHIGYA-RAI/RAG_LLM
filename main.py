from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException
app = FastAPI()

''' Validation
@app.post("/documents/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="You can only upload PDF files.😅")
    return {"Filename" : file.filename}
'''
import fitz
'''@app.post("/documents/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="You can only upload PDF files.😅")
    data = await file.read()
    doc = fitz.open(stream=data,filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    return {
        "Filename" : file.filename,
        "Page count" : len(doc),
        "Character count": len(text),
    }'''

from pydantic import BaseModel
class DocumentInfo(BaseModel):
    filename: str
    page_count:int
    character_count:int
@app.post("/documents/upload",response_model=DocumentInfo)
async def upload(file:UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="You can only upload PDF files.")
    data = await file.read()
    doc = fitz.open(stream=data,filetype="pdf")
    text = "".join(page.get_text() for page in doc)

    return DocumentInfo(
        filename = file.filename,
        page_count = len(doc),
        character_count = len(text),
    )


