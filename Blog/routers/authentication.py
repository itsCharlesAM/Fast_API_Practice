from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .JWT_token import create_access_token
import schemas
from sqlalchemy.orm import Session
from db_conn import SessionLocal, get_db
import models
from passlib.context import CryptContext


router = APIRouter(
    tags=["login"]
)  

#password Encryptionr
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifyPassword(plain_password, hashed_password):
    return pwd_context.verify (plain_password, hashed_password)

#login
@router.post('/login' )
def login(request :OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    if not verifyPassword( request.password ,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password not correct")

    #Generate a JWT token and return it
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"} 
