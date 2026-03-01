# backend/app/schemas.py
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, field_validator

from .core.utils import normalize_message


class GuestbookEntryIn(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def normalize(cls, value: str) -> str:
        return normalize_message(value)


class GuestbookEntryOut(BaseModel):
    id: int
    message: str

    model_config = ConfigDict(from_attributes=True)

    @field_validator("timestamp", mode="after")
    @classmethod
    def ensure_utc(cls, value: datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value
