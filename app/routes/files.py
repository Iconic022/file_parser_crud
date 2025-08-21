from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
import aiofiles
import os
from ..database import SessionLocal
from .. import crud, models, tasks, schemas

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/files", response_model=schemas.FileResponse)
async def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    db_file = crud.create_file(db, file.filename)
    file_path = os.path.join(UPLOAD_DIR, db_file.id + "_" + file.filename)

    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    tasks.parse_file.delay(db_file.id, file_path)
    return db_file

@router.get("/files/{file_id}/progress", response_model=schemas.FileResponse)
def get_progress(file_id: str, db: Session = Depends(get_db)):
    return db.query(models.File).filter(models.File.id == file_id).first()

@router.get("/files/{file_id}", response_model=schemas.FileContent)
def get_file(file_id: str, db: Session = Depends(get_db)):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if file.status != "ready":
        return {"message": "File upload or processing in progress. Please try again later."}
    return file

@router.get("/files", response_model=list[schemas.FileResponse])
def list_files(db: Session = Depends(get_db)):
    return db.query(models.File).all()

@router.delete("/files/{file_id}")
def delete_file(file_id: str, db: Session = Depends(get_db)):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
    return {"message": "Deleted"}
