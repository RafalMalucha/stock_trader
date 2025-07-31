import uuid
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True