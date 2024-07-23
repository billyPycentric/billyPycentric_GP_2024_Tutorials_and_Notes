### trying out encapsulation with python
## Hiding variables of methods , using setters and getters

class Person:
    def __init__(self , name , age , height):
        self.__name= name
        self.__age = age
        self.__height = height
    ## create a property to access these private fields
    def get_name(self):
        return self.__name
    def set_name(self , name):
        self.__name  = name

p1 = Person("Abongile",25,1.7)

print(p1.get_name())
p1.set_name("billy")
print(p1.get_name())
print(p1.name())

my_list = [1,3,5,3]
my_list.insert(2,4)