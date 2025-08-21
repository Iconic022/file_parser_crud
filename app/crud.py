import uuid
from sqlalchemy.orm import Session
from . import models

def create_file(db: Session, filename: str):
    file_id = str(uuid.uuid4())
    db_file = models.File(id=file_id, filename=filename)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def update_progress(db: Session, file_id: str, progress: int, status: str):
    db_file = db.query(models.File).filter(models.File.id == file_id).first()
    if db_file:
        db_file.progress = progress
        db_file.status = status
        db.commit()
        db.refresh(db_file)
    return db_file

def save_content(db: Session, file_id: str, content: str):
    db_file = db.query(models.File).filter(models.File.id == file_id).first()
    if db_file:
        db_file.content = content
        db_file.status = "ready"
        db_file.progress = 100
        db.commit()
        db.refresh(db_file)
    return db_file
