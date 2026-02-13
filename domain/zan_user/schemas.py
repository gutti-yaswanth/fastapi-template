from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ZanUserCreate(BaseModel):
    phone: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    is_zancrew: Optional[str] = "false"
    zancrew_id: Optional[int] = None

class ZanUserUpdate(BaseModel):
    phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    is_zancrew: Optional[str] = None
    zancrew_id: Optional[int] = None

class ZanUserResponse(BaseModel):
    user_id: int
    phone: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    is_zancrew: Optional[str] = None
    zancrew_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

