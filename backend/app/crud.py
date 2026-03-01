# backend/app/crud.py

# Kommentar: CRUD står för Create, Read, Update, Delete och innehåller
# funktioner för att interagera med databasen, som anropas från routrar.

from sqlalchemy.orm import Session

from .models import GuestbookEntry


def get_entries(db: Session):
    """Get all guestbook entries."""
    return db.query(GuestbookEntry).all()


def register_entry(db: Session, message: str) -> GuestbookEntry | None:
    """Register new guestbook entry."""

    entry = GuestbookEntry(message = message)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def delete_entry(db: Session, id: int) -> bool:
    """Delete entry."""
    entry = db.get(GuestbookEntry, id)
    if entry is None:
        return False

    db.delete(entry)
    db.commit()
    return True


#Add patch too
