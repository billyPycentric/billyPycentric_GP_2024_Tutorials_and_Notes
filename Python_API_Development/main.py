from typing import Optional
from fastapi import FastAPI , status , Response
from fastapi.params  import Body
from pydantic import BaseModel
from routers import authentication
from routers import person
import hashpasswords

app = FastAPI() 
import sys

app.include_router(person.router)
#app.include_router(authentication.router)


## @ is for a decorator .get is an HTTP request("path")
##Ccreating a schema



@app.get("/persons/names")
async def root():
    return {
        "name":{
            "ifalanga",
            "Khanyi" ,
            "billy",
            "Vhutali"
        }
        }
@app.get("/about" , status_code=status.HTTP_302_FOUND)
async def about_page():
    print(hashpasswords.hash_password())
    return "This is about page , basically"

# @app.get("/persons/{id}")
# async def get_person(id : int):
#     return f"You selected {id} , now here is the list"

# # Experimenting wuth query paramaters
# @app.get("/who")
# async def getAll(limit:int,employable :bool = False):
#     if employable == True:
#         return f"This is the limit: '{limit}' that was passed into the url and they are employable"
#     return "Returning all persons in the database"


























# Creating a post-req
