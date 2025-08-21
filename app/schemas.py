from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FileBase(BaseModel):
    filename: str

class FileResponse(FileBase):
    id: str
    status: str
    progress: int
    created_at: datetime

    class Config:
        orm_mode = True

class FileContent(FileResponse):
    content: Optional[str]
