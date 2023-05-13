from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import shutil
app = FastAPI()

@app.get("/")
def inde():
    return {"message": "welcome FastAPI nerds"}

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/upload/")
async def create_upload_file(file: UploadFile= File(...)):
    with open("uploads/file.pdf","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}