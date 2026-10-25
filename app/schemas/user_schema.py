from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    name: str
    last_name: str
    email: str
    

class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: str
    is_activate: bool
    is_verified: bool
    created_at: datetime
