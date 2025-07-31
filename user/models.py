import uuid
from sqlalchemy import Column, String, Integer
from database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True, unique=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(64), nullable=False, unique=True)