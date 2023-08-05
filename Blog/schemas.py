from pydantic import BaseModel

#request model
class BlogModel(BaseModel):
    title : str
    body : str


class User(BaseModel):
    name : str
    email : str
    password : str


class UserEdit(BaseModel):
    name : str
    email : str



#response User model
class ShowUser(BaseModel):
    name : str
    email : str
    blogs : list[BlogModel]


#response model
class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUser


#request for login
class loginRequest(BaseModel):
    username : str #email
    password : str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

