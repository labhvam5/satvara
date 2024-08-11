from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from db import get_db
from sqlalchemy.orm import Session
from models import User
from utils import verify_password
from oauth2 import create_access_token

router = APIRouter(
    tags=["Auth"]
)

@router.post("/login")
def login(user_creds: Annotated[OAuth2PasswordRequestForm, Depends()], db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_creds.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify_password(user_creds.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = create_access_token(data = {"user_id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
