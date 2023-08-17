# from fastapi import APIRouter, Depends, HTTPException, Response, status
# from operator import and_
# import oauth2
# import schemas
# from db_conn import get_db
# import models
# from sqlalchemy.orm import Session
# from passlib.context import CryptContext

# router = APIRouter(
#     prefix='/user',
#     tags=["user"]
# )

# #password Encryption for user
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# #srote users in database
# @router.post('/' ,  status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
# def create_user(request: schemas.User_req, db: Session = Depends(get_db)):
#     hashed_password = pwd_context.hash(request.password)
#     new_user = models.User(
#         name=request.name,
#         email=request.email, 
#         password=hashed_password
#     )
#     db.add(new_user)
#     db.commit()  
#     db.refresh(new_user)

#     return new_user

# #get data from database - get specified User by id
# @router.get('/{id}',  response_model=schemas.ShowUser)
# def show(id, db: Session = Depends(get_db)):
#     sel_user = db.query(models.User).filter(models.User.id == id).first()

#     if not sel_user: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
#     return sel_user


# #Update user data 
# @router.put('/{id}', response_model=schemas.UserEdit)
# def update (id, response : Response, request : schemas.UserEdit, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    
#     user = db.query(models.User).filter(
#         and_(
#             models.User.id == id,
#             models.User.email == current_user.username
#         )
#     ).first()

#     if not user: 
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return "User not found!"
    
#     user.name = request.name
#     user.email = request.email

#     db.commit()
    
#     return user
