from celery import Celery
from time import sleep
from .database import SessionLocal
from .crud import update_progress, save_content

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def parse_file(file_id: str, file_path: str):
    db = SessionLocal()
    for i in range(1, 6):
        sleep(2)
        update_progress(db, file_id, i * 20, "processing")

    with open(file_path, "r") as f:
        content = f.read()
    save_content(db, file_id, content)
    db.close()
