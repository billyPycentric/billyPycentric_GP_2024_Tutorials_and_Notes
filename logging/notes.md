# Basics Of Logging   
1. **DEBUG**   -> Detailed info

2. **INFO**   -> Confirmation that everything is working as expected

3. **WARNING**  -> The Code is working but there might be a potential problem in the future

4. **ERROR**     ->  Due to more serious problems , the functions cannot be performed

5. **CRITICAL**   -> The program may be unable to continue   
## Create First Logs   
~~~python
import logging

logging.basic.Config(filename='test.log',level=logging.DEBUG)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b
a=6
b=3
add_result = add(a,b)
logging.warning('Add:{} + {} = {}'.format(a,b,add_result))

sub_result = subtract(a,b)
logging.warning(f"Sub : {a} - {b} = {sub_result}")

multiply_result = multiply(a,b)
logging.warning(f"Sub : {a} * {b} = {multiply_result}")

divide_result = divide(a,b)
logging.warning(f"Sub : {a} / {b} = {divide_result}")


### Expected Results   
WARNING:root:Add:6 + 3 = 9
WARNING:root:Sub : 6 - 3 = 3
WARNING:root:Sub : 6 * 3 = 18
WARNING:root:Sub : 6 / 3 = 2.0

~~~   
## Docs for Logs format   
Here is the link :   
[Python Docs](https://docs.python.org/3/library/logging.html#logrecord-attributes)   
