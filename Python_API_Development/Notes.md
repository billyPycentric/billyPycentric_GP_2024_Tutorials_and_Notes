# Python API Development
1. Create a Virtual Environment   
~~~
python3 -m venv venv
~~~   
2. Navigate into the V.Env   
~~~
venv/Scripts/activate   -> to activate it(windows)
~~~   
3. Select the venv intepreter   
~~~
click view on VSCode , Command Palette , select Python interpreter , then choose venv
~~~   
4.Install Fast API   
~~~
pip install fastapi[all]  -> also going to install all the dependencies you might need

//Check all the depenndencies
pip freeze
~~~   
## Fast API  
creating a basic web application   
~~~python
# importing the FastAPI class from fastapi
from fastapi import FastAPI

# Create an instance of the application store it in a variable
app = FastAPI()

# Now to handle the HTTP request
#@app decorator -> which with the path

@app.get("/") -> default "path"
async def data():
    return {
     "name" : {
          "Abongile",
          "ifalanga" , 
          "Vhutali" , 
          "Khanyi"
}


}
~~~
## Types of HTTP-requests   
1. PUT -> replaces the curr resource   
2. DELETE -> deletes the curr resource   
3. POST -> creates a resource   
4. HEAD -> same as "GET" , with no response body   
5. OPTIONS -> describe communnication options to target resource    
## HTTP Request   
already used app.get()   
~~~python
# using post 
async def add_user(requestBody : dict = Body(...)):
    return {"success" : f"new user '{requestbody["name"]}' is added"}
~~~   
## Schemas   
they are used to provide structure and validation of the data the API send/recieves in python we use ***pydentic*** library for that   
~~~python
# suppose you wanted a user , with the following fields
# name , surname , age  , employeed and qualification

# 1. Need to import BaseModel from pydentic
# 2. create a class for the model/structure

from pydentic import BaseModel

## Class

class Person(BaseModel):
   name: str
   surname: str
   age: int
   employed: bool
   qualification: str

## And on your POST Req
@app.post("/path")
async def add_person(person_body : Person):
     return person_body
    

## i LOkked at Optionals too
name:Optional[datatype] = 3

~~~   
## C R U D    
Create , Read , Update and Delete   
1. **Create(POST)** -> path="/+plural" i.e for user you would use path="/users" its a standard naming convention      
2. **Read(GET)** -> by {id} or all  
* {id} -> path="/users/{id}"   
* all -> path="/users"   
3. **Update(PUT)** -> {id} -> path="/users/{id}"  
4. **Delete(DELETE)** -> {id} -> path="/users/{id}"   

## HTTP Status_Codes   
1. 1XX(INFORMATION) -> server ackmoledges and is processing the request   
2. 2XX(SUCCESS) -> Server recieved and successfully understood the request
3. 3XX(REDIRECTION) -> Server recieved the request but it got redirected
4. 4XX(CLIENT ERROR) -> Couldnt find the Site
5. 5XX(SERVER ERROR) -> Client made a Valid req but the server wasnt able to complete it
   
