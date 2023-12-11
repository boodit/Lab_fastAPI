from typing import Union,Annotated
from pydantic import BaseModel,Field,HttpUrl

class Person(BaseModel):
    lastName: str = Field(default="lastname",min_length=3,max_length=25)
    age: int = Field(default=100,ge=10,le=200)

class Good(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[str, None] = None
    nalog: Union[str, None] = None

class Main_User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int,None], Field(default= 100, ge=1,lt=200)] = None

class Main_UserDB(Main_User):
    password: Annotated[Union[str, None], Field(max_length=200,min_length=3)]=None

class New_Response(BaseModel):
    message: str