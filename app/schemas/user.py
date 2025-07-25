from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str    
    
class userOut(BaseModel):
    id: int
    username: str
    
    class Config:
        form_mode = True    