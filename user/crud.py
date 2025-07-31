import uuid

from sqlalchemy.orm import Session
from sqlalchemy.exc import InvalidRequestError, IntegrityError

from user import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.UserModel).filter(models.UserModel.username == username).first()

def create_user(db: Session, user_in: schemas.UserCreate):
    user = models.UserModel(username=user_in.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user