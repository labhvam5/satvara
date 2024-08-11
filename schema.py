from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True
    rating: Optional[int] = None

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    rating: Optional[int] = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    rating: Optional[int] = None
    user_id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
