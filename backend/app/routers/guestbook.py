# backend/app/routers/competitors.py
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..database import get_db
from ..schemas import GuestbookEntryIn, GuestbookEntryOut

router = APIRouter(prefix="/guestbook", tags=["times"])


@router.get("", response_model=list[GuestbookEntryOut])
def read_messages(db: Annotated[Session, Depends(get_db)]):
    """Get all entries."""
    return crud.get_entries(db)


@router.post("/record", response_model=GuestbookEntryIn)
def record_time(data: GuestbookEntryIn, db: Annotated[Session, Depends(get_db)]):
    """Post a new entry."""
    entry = crud.register_entry(db, data.message)
    if entry is None:
        raise HTTPException(status_code=404, detail="Competitor not found")
    return entry
