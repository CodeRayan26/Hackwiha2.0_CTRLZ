from typing import Optional
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    account_type: Optional[str] = None

class UserOut(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    account_type: str
    role: str  # added field

    class Config:
        orm_mode = True

# Feed Content Schemas
class FeedContentBase(BaseModel):
    creator_id: int
    title: str
    content: str
    content_type: str

class FeedContentCreate(FeedContentBase):
    pass

class FeedContent(FeedContentBase):
    content_id: int
    is_featured: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True