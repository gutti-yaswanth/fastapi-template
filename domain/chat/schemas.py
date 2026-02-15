from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


# --- Participant type: used in DB and API ---
ParticipantType = Literal["zan_user", "zan_crew"]


class ChatRoomResponse(BaseModel):
    id: int
    job_id: int
    is_read_only: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ChatMessageCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=16_000)


class ChatMessageResponse(BaseModel):
    id: int
    chat_room_id: int
    sender_type: str  # zan_user | zan_crew | system
    sender_zan_user_id: Optional[int] = None
    sender_zancrew_id: Optional[int] = None
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class ChatMessagesPage(BaseModel):
    messages: list[ChatMessageResponse]
    next_cursor: Optional[str] = None
    has_more: bool
