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
There are different ways in which we can perform tests   
### We can have ***Function*** or  ***Class*** based test   
1. **Function** based : 
~~~python
## going to need @pytest.fixture -> avoid code duplication
# super class , using shapes in this example
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
# sub class , wich will extend the super class
class NameOfShape(Shape):
    # def the __init__ func -> acts as a constructor
    def ___init__(self , field_for_shape1 ,field_for shape2, ...):   
        # Here we setting out variables
        self.field_for_shape1 = field_for_shape1
    # Now you can overide the methods in the parent/super class
    # supposed you had a rectangle as a shape , an area as a method you want to overide , this is how you will go about it

    def area(self ,length ,width):
        return length*width

# Now go on the test_file
## using this test file for TEST by FUNCTION
import pytest
import source.shapes as shapes

def test_area():
    rhombus = shapes.Rhombus(4,6)
    assert rhombus.area() == 4*6

# Testing the perimeter
def test_perimeter():
    rhombus = shapes.Rhombus(4,6)
    assert rhombus.perimeter() == (2*4) + (2*6)
~~~  
2. **Class** based :  
going to need :   
* Super Class
* Sub Class
* Test Class 
~~~python
# super class , using shapes in this example
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
# sub class , wich will extend the super class
class NameOfShape(Shape):
    # def the __init__ func -> acts as a constructor
    def ___init__(self , field_for_shape1 ,field_for shape2, ...):   
        # Here we setting out variables
        self.field_for_shape1 = field_for_shape1
    # Now you can overide the methods in the parent/super class
    # supposed you had a rectangle as a shape , an area as a method you want to overide , this is how you will go about it

    def area(self ,length ,width):
        return length*width

## Test Class
# you going to have a setup method and teardown method

# here is your area_test
def area_test(self):
    # results from the sub class -> your Area
    result = self.rectangle.area()
    # compare it with expected -> perform calc now
    expected = self.rectangle.length * self.rectangle.width
    ## if the obove statement is true then the test will pass

~~~   
## Parametirizing   
> Here you want to test same function but x number of times   
how to use it :   
~~~
# need @pytest.mark.parametirize annotation
# gonna nee the arguments , result also the expected_output

@pytest.mark.parametirize("result , expected_output" , [("result","expected_output"),("result" , "expected_output")])
def mutliple_tests_for_func(results , expected_output):
    #assign your results an expected_output
    # then assert
    assert result == expected_output
~~~