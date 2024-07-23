# adding two numbers / variable
def add(a, b):
    return a+b

# dividing two numbers
def divide(a, b):
    if( b ==0):
        raise(ValueError)
    return a/b