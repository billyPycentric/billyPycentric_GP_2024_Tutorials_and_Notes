## Python From Scratch
-> It is high level language wich uses an Intepreter(low level - mean Machine Oriented)

## New Concepts   
> Enums   
~~~python
# represent a set of related constants
from enum import Enum

# Make a Class
class se    tConstants(Enum):
    TRUE = 0
    FALSE = 1   # All Caps -> Constant Var
  
~~~    
## Lists
~~~python
names = ["Abngile" , "Billy"]
data = ["Abongile" , True , 45 , 55.3]
~~~   
### Sclizing in Python   
~~~python

# Supposed we have 
list = [1,2,3,4]
# if we use -> list[1,3] , we will be replacing contents from 1 till 2 but if  list[1,3] = [7,4,3,7,9] , goes above the slice req then anything after 1 and 2 wont be replaced




~~~   
## Dictionary  
basically your json data   
~~~
interns = {
    "name":"abongile",
    "age":"24",
    "vocals":"yes",
  

}
They are actually different , but simialr 
just that in python keys can be of any type from string,boolean , int , double
~~~   
## Nested Dictionary   
suppose we have a gym_members dict   
each member has name location and surname:   
~~~python
#declare a dict
gym_members = {

}

# now decl members
member1 = {
    "name" : "Abongile",
    "surname" : "billy",
    "location" : "vaal",
    }
member2 = {
    "name" : "Ifalanga",
    "surname" : "surname_forgot",
    "location" : "Johannesburg",
    }
member3 = {
    "name" : "Khanyi",
    "surname" : "surname_Long",
    "location" : "Pretoria"
    }
### now add them 
gym_members = {
    "member1" : member1,
    "member2" : member2,
    "member3" : member3
}   

~~~   

## Recursion   
Func that calls it self   
> Demo -> Structure   
> func
> break , break out of func
> call func   
### Notes   
### Notes
~~~python
def walk(steps):
    if steps ==0:
        return
    
    steps-=1
    walk(steps)
    print(steps)
##  This function takes steps as an argument and will display the steps walked/taken
 if step =2 then : 
walk(2) -> step =1 then call walk(1)
walk(1) -> step =0 then terminates   
then it will go to the call stack - uses LIFO  

~~~   
#### LIFO and FIFO   
theyy are both data-structures used to manage and manipulate data   
on Fifo -> an element is inserted using en-queue and poped out used de-queue   

### Recursion Vs Factorial  
recursion is simpler to write but it can be slower and the call stack storage or spaces are limited  to 996 i think   

## Closure  
When a child function has access to vars in the parent function   
~~~python

def parent(parent):
    no_of_houses = 3

    def child():
        nonlocal no_of_houses -=1
    ## We are basically able to access the parents resources by using the nonlocal term
~~~   

## f_Strings   
Use it to embed expressions in strings provide an easy and readable way to format strings   
~~~python
# This is the usual structure
 # put f in front of every string you want to embed and use {} to insert $
 name = "Abongile"
 profession = "Software Development Engineer"
 
 about_me = f"Hi my name is {name} and i am a {} who has 0 experience unfortuantely"
~~   
~~~python
# About Me
about = {
    "name" : "Abongile",
    "Surname":"Billy" , 
    "Varsity": {
        "Name" : "North West University",
        "Course" : "BSc Computer Science And Economics"
        },
    "Profession": "Software Development Engineer",
    "Experince":" Less than A Year",
    "Coding Languages":{
        "Backend" :{
            "Languages" : "Python , Java",
            "Frame-Works" : "FastAPI , Spring"
        },
        "Web" : "HTML , javascript , typescript"

    },
    "Married" : False 
}

~~~   
~~~python

about_message = f""" Hi my name is {about['name']} {about['Surname']} and i am {str(25) + " years old (Dont know why i fogot to mention that)"} , 
I attended {about['Varsity']["Name"]} did the course {about['Varsity']["Course"]}  i am a {about['Profession']} currently have {about['Experince']} 
and i know these languages : {about['Coding Languages']['Backend']["Languages"]} for back end with framworks {about['Coding Languages']['Backend']["Frame-Works"]}

"""

print(about_message)
~~~   
## Modules
~~~python
#A file that contains set of functions you would want to use
# modules already familiar with
import math  # use from math import pi -> using an alias

#to use a function from the module
#use . to the the list of funcs associated with the module-> alias
use #dir() func to get a list of funcs associated with that module
dir()
~~~    
## Object Oriented Programming   
The way of thinking about and organizing code for a maximum reusability , use objects for that.    
> 4 Core features for OOP  
# 
1. Encapsulation , hiding data and method complexities   
2. Polymorphism , allows methods to process objs differently because of their data type ***overloading/overriding***   
3. abstraction , showing only essential information not everything   
4. Inheritance , creating a new obj with properties of an existing obj   
~~~python
### Inheritance  
class Vehicle:
    ## This is also a constructure -> you can also give it defalut values
   ##self is the current instance of a class
    def __init__(self , make ,model ,manufacturer):
        self.make = make
        self.model = model
        self.manufacturer = manufacturer   
   def moves(self):
       print("I am Moving")
       ## What should i use , return or print
class Car(Vehicle):
    def __init__(self , make, model ,manufacturer , type):
        super().__init__(make,model,manufaturer)
        self.type = type
## Creating an instance
car1 = Car("tesla","model x","tesla motors","Eletric")   
## when i were to creat another class lerts say called bus 
## bus1 = (#variables) then it would show polymoorphism

    
~~~   
~~~python
## Abstraction is the same as making an interface

suppose i created another method in the above class for Vehicles , method that told me if the Vehicle is on land/sea/air , since the method is found in all of the child classes then it should be

## encapsulatioin
use __var to make the fields private 

class Person():
    def __init(self, name):
        self.__name = name
    def get_name():
      return self.__name
    def set_name(self,name):
       self.__name= name   



~~~   
## Files
Use RAWX -> read"r" ,append"a" , write"w" and create"x"
~~~python
#open a file
File = open("filename.extension","r/w/x/a")
remember to close after
file.close

#can also use try and except when try to open a file
try:
 ## Open a file
except:
    ## file you want to open does not exist

#deleting
if os.path.exist("filename.txt"):
    os.remove("filename.txt")

# creating a file

if not os.path.exist("filename.txt"):
    file = open("filename.txt" ,"x")


~~~    
## ***Lambdas*** and higher order func    
**lambdas** is a one line func -> lamba var:var+1 return "x"   
We use lambdas for functional programming -> function passed as parameters   
~~~ python
# lambda func for adding a and b
add_nums = lambda a,b:a+b
print(add_nums(a,b))   



## Higher Order funcs -> return functions or take them as arguments
## allow us to write more concise code  
def func_builder(a):
    return lambda b:a**b


square = func_builder(3)
print(square(2))
~~~  
   



