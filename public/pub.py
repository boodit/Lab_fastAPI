import uuid
from fastapi import FastAPI, Body, APIRouter
from fastapi.responses import JSONResponse,FileResponse
from models.good import Main_User,Main_UserDB,New_Response
import hashlib
from typing import Union,Annotated

user_router = APIRouter()

def code_passwd(cod:str):
    result = cod * 2

user_list = [Main_UserDB(name = "Antonov",id = 3,password="5580"),Main_UserDB(name = "Alexeev",id = 5,password="565580")]

def find_user(id:int)->Union[Main_UserDB,None]:
    for user in user_list:
        if user.id == id:
            return user
    return None

@user_router.get("/api/users",response_model=Union[list[Main_User],None])
def get_users():
    return user_list

@user_router.get("/api/users/{id}",response_model=Union[Main_User,New_Response])
def get_user(id:int):
    user = find_user(id)
    print(user)
    if user == None:
        raise New_Response(message="Not found")
    return user

@user_router.post("/api/users",response_model=Union[Main_User,New_Response])
def create_user(item:Annotated[Main_User,Body(embed=True,description="new user")]):
    user = Main_UserDB(name=item.name,id=item.id,password=code_passwd(item.name))
    user_list.append(user)
    return user

@user_router.put("/api/users",response_model=Union[Main_User,New_Response])
def edit_person(item:Annotated[Main_User,Body(embed=True,description="changed user from id")]):
    user = find_user(item.id)
    if user == None:
        raise New_Response(message="not found user")
    user.id = item.id
    user.name = item.name
    return user

@user_router.delete("/api/users/{id}",response_model=Union[list[Main_User],None])
def delete_person(id: int):
    user = find_user(id)
    if user == None:
        return New_Response(message="not found user")
    user_list.remove(user)
    return user_list