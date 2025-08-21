from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime
from .database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, index=True)
    filename = Column(String, index=True)
    status = Column(String, default="uploading")
    progress = Column(Integer, default=0)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
