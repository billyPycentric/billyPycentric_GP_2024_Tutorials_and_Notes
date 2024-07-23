from dataclasses import dataclass
import functools
#Dont want to pass the self argument
# any method that desn tinteract with the instance of the self var
class Math:
    @staticmethod
    def sub(a,b):
        return a-b


### Class Methods
### getting everything that is defined in the class not using instances
class Person():
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        return cls.species

########### Functools
@functools.cache
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2) 

print(fibonacci(3))



#######################
# dataclass decorator
# works like lombok
@dataclass
class Product:
    name : str
    price : float
    quantity : int
    def total_cost(self):
        return self.price * self.quantity




