from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostsCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    create_at: datetime
    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    create_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr
    password:str



class UserLogin(BaseModel):
    email: EmailStr
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: Optional[str] = None