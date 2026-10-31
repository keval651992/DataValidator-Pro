from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
  id: int = Field(..., gt=0)
  name: str
  username: str
  email: EmailStr
  phone: Optional[str] = None
  website: Optional[str] = None