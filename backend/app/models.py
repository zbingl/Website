# backend/app/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class GuestbookEntry(Base):
    __tablename__ = "Guestbook entries"
    id = Column(Integer, primary_key=True, index=True)
    message: Mapped[str] = mapped_column(String)
