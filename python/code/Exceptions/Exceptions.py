## I am going to look at Exceptions
## Exceptions are raised in Python

class BillyError(Exception):
    pass


x = 45
try:
    #print(x)
    if type(x) is str:
        raise BillyError("only numbers are allowed ! , from Billys Custom Exception")
except NameError:
    print("NameError means somthing is probably undefined")
except Exception as error:
    print(error)
except ZeroDivisionError:
    print("ZeroDivisionError , you cannot divide by Zero")
else:
    print("No , Errors !")

finally : 
    print("This is the final block")