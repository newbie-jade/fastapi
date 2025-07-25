from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostsCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    create_at: datetime
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserOut(BaseModel):
    id:int
    email:EmailStr
    create_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password:str
