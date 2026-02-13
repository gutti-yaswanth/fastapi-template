from pydantic import BaseModel, Field
from typing import Optional

class SendOTPRequest(BaseModel):
    phone: str = Field(..., description="Phone number in E.164 format (e.g., +1234567890)")

class VerifyOTPRequest(BaseModel):
    phone: str = Field(..., description="Phone number in E.164 format (e.g., +1234567890)")
    token: str = Field(..., description="OTP token received via SMS")

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: dict
    expires_in: Optional[int] = None
    token_type: str = "bearer"

class SendOTPResponse(BaseModel):
    message: str
    phone: str

