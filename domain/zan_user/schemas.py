from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ZanUserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    is_zancrew: str = "false"
    zancrew_id: Optional[int] = None

class ZanUserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_zancrew: Optional[str] = None
    zancrew_id: Optional[int] = None

class ZanUserResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    is_zancrew: str
    zancrew_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

