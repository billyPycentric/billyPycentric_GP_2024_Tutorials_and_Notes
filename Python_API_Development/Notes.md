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

