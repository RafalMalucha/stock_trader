from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from user import models, schemas, crud
from database import engine, SessionLocal, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "hello"}

@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user)