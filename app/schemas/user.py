from pydantic import BaseModel


class UserCreate():
    username: str
    password: str
    
class UserLogin():
    username: str
    password: str    
    
class userOut():
    id: int
    username: str
    
    class Config:
        form_mode = True    