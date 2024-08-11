from fastapi import Depends, HTTPException, status, APIRouter
from schema import UserCreate, UserResponse
from db import get_db
from sqlalchemy.orm import Session
from models import User
from utils import get_password_hash

router = APIRouter(
    tags=["Users"]
)

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate ,db: Session = Depends(get_db)):
    print(user)
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
