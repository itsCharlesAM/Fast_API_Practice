# from fastapi import FastAPI, File, HTTPException, UploadFile, APIRouter, status, Depends
# from sqlalchemy.orm import Session
# from db_conn import SessionLocal, get_db
# import oauth2
# import os
# import shutil
# from typing import List
# from models import User

# router = APIRouter(
#     tags=["image"]
# )

# UPLOADS_DIR = "uploads"
# ALLOWED_EXTENSIONS = {"png", "jpeg", "jpg"}

# @router.post('/upload')
# async def upload_image(
#         file: UploadFile = File(...),
#         db: Session = Depends(get_db),
#         current_user : User = Depends(oauth2.get_current_user)
#     ):

#     user = db.query(User).filter(User.email == current_user.username).first()

#     # Create the 'uploads' directory if it doesn't exist
#     os.makedirs(UPLOADS_DIR, exist_ok=True)

#     # Check if the uploaded file has an allowed extension
#     file_extension = file.filename.split(".")[-1]
#     if file_extension.lower() not in ALLOWED_EXTENSIONS:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file format. Allowed formats: PNG, JPEG, JPG")

#     # Construct the file path for saving
#     file_name = f"{user.id}.{file_extension}"
#     file_path = os.path.join(UPLOADS_DIR, file_name)

#     # Save the uploaded image
#     with open(file_path, 'wb') as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     user.profile_img = file_path
#     db.commit()

#     return {"message": "File uploaded successfully"}



# @router.delete('/delete')
# async def delete_image(
#         db: Session = Depends(get_db),
#         current_user: User = Depends(oauth2.get_current_user)
#     ):

#     user = db.query(User).filter(User.email == current_user.username).first()

#     # Construct the file paths for the allowed extensions
#     file_extensions = ["png", "jpeg", "jpg"]
#     deleted = False

#     for extension in file_extensions:
#         file_path = os.path.join(UPLOADS_DIR, f"{user.id}.{extension}")
        

#         # Check if the image file exists
#         if os.path.exists(file_path):
#             os.remove(file_path)
#             deleted = True

#     if deleted:

#         user.profile_img = None
#         db.commit()

#         return {"message": "Image deleted successfully"}
#     else:
#         # return file_path

#         raise HTTPException(status_code=404, detail="Image not found")
