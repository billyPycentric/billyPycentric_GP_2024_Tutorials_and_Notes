# Code Testing   
Code testing refers to running each line of code with a controlled output and verify if it performs the expected output, and there are different types of ***CODE TESTING*** :    
* Unit Testing
* Integration Testing
* System Testing
> Why Code testing   
It ensures that there is sustainability , maintainability and reliability in software solutions   
# Code Testing in Python'
## Using pytest  
### Install pytest   
1. Create a Virtual Environment   
~~~
python -m venv venv
~~~   
2. Install pytest   
~~~
pip install pytest
~~~   
3. Check if pytest is Installed   
~~~
pytest --version 
~~~
4. Activate the Enviroment   
~~~
// for Windows
venv/Scripts/activate 
~~~   
### Simple Test
Create 2 directories , for both tests  and source , i.e test.py , main.py   
1. For main.py:   
~~~python
// for adding 2 variables
def add(a , b):   
    return(a+b)   
   
// for dividing 2 variables -> numbers   
def divide(a,b):   
// throw an exception if b=0    
    if(b == 0):
      raise(ValueError)
   


~~~   
2. For test.py   
~~~
// need to import pytest
import pytest
// also dont forget to import relevant files/directories

// write a test func for add
def test_add():
     // we are going to give it controlled inputs
     result = main.add(1,3)
     // we know result is going to be 4
     assert result == 4
def test_divide():
     with pytest.raises(ValueError):
          main.divide(1,0)



~~~