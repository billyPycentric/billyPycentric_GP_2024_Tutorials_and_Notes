# Decorators
1. Propert -- ---> @property   
~~~
'''decorator in Python is used to define methods in a class that can be accessed like attributes. This allows for more control over how attributes are accessed and modified, encapsulating the logic within getter, setter, and deleter methods.'''

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

person1 = Person("Abongile")
print(person.name)  # Getter
person2.name = "Ifalanga"  # Setter
print(person.name)
del person.name  # Deleter

~~~
2. staticMethods ->@ staticmethod   
~~~ python
'''
decorator in Python is used to define methods that belong to a class but do not access or modify the class state. These methods do not require a reference to an instance or the class itself and are mainly used to group functions that logically belong to the class
'''   
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

~~~
3. classMethods -->@classmethod   
~~~python
'''
is used to define methods that are bound to the class and not the instance of the class. These methods can access and modify class state that applies across all instances of the class. The first parameter of a class method is typically named cls, which refers to the class itself
'''

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()

    @classmethod
    def increase_population(cls):
        cls.population += 1

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")


~~~
4. Data class -----> @dataclass
~~~python
from dataclasses import dataclass

'''
is used to automatically generate special methods for classes, such as __init__, __repr__, __eq__, and __hash__. It simplifies the creation of classes that are primarily used to store data by reducing boilerplate code
'''

@dataclass
class Person:
    name: str
    age: int
    email: str = ""

~~~
4. functools  ---->@functools.cache   
~~~python
import functools

'''
is used to cache the results of a function call based on its input arguments. This can significantly improve performance by avoiding redundant computations for the same input
'''
@functool.cache


~~~
