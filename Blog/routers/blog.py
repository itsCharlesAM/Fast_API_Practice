from fastapi import APIRouter, Depends, HTTPException, Response, status
from schemas import ShowBlog, BlogModel, User
import oauth2
from db_conn import SessionLocal, get_db
from models import Blog, User
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/blog',
    tags=["blog"]
)


#srote data in database
@router.post('/showlogedUser' , status_code=status.HTTP_201_CREATED)
def showlogedUser(db: Session = Depends(get_db),  current_user : User = Depends(oauth2.get_current_user)):

    user = db.query(User).filter(User.email == current_user.username).first()

    return user.id


#srote data in database
@router.post('/' , status_code=status.HTTP_201_CREATED)
def create_blog(request : BlogModel, db: Session = Depends(get_db) ,current_user : User = Depends(oauth2.get_current_user) ):
    
    user = db.query(User).filter(User.email == current_user.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    # user = db.query(User).filter(User.email == current_user.username).first()

    new_blog = Blog (title = request.title, body = request.body, user_id = user.id)  
    db.add (new_blog)
    db.commit()
    db.refresh(new_blog)  
    return new_blog

 
 
# get data from database
@router.get('/',  response_model=list[ShowBlog] )    
def all(db: SessionLocal = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    blogs = db.query(Blog).all()
    return blogs




#get data from database - get specified blog by id
@router.get('/{id}',  response_model=ShowBlog)
def show(id, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    sel_blog = db.query(Blog).filter(Blog.id == id).first()

    if not sel_blog: 
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return sel_blog


#delete data from database
@router.delete('/{id}')
def delete (id, response :Response, db: Session = Depends(get_db),current_user : User = Depends(oauth2.get_current_user)):
    sel_blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    db.commit() 

    if not sel_blog: 
        response.status_code = status.HTTP_404_NOT_FOUND
        return "Blog with the specified id not found!"
    
    response.status_code = status.HTTP_200_OK
    return "Blog deleted from Database"



#Update data 
@router.put('/{id}', response_model=ShowBlog)
def update (id, response : Response, request : BlogModel, db: Session = Depends(get_db), current_user : User = Depends(oauth2.get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog: 
        response.status_code = status.HTTP_404_NOT_FOUND
        return "Blog with the specified id not found!"
    
    blog.title = request.title
    blog.body = request.body
    db.commit()
    
    return request
