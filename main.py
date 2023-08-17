from fastapi import FastAPI
# from db_conn import engine
# import models
# from routers import blog, user,authentication, image, email

app = FastAPI()
     
# models.Base.metadata.create_all(bind=engine)

# app.include_router(authentication.router) 
# app.include_router(blog.router) 
# app.include_router(user.router) 
# app.include_router(image.router)
# app.include_router(email.router)

@app.post("/")
async def root():
    return {"message": "Hello World"}