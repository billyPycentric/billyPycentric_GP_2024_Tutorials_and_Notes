## OOP

class Granny():
    def __init__(self , age,name):
        self.age = age
        self.name = name
    def message(self):
        return "I am old buddy"
    def new(self):
        return "My nam eis "
    def get_age(self):
        return self.age

class Mother(Granny):
    def __init__(self ,babies,my_age, name,age):
        super().__init__(age,name)
        self.my_age  = my_age
        self.name = name

    def message(self):
        return f"I am a mother my moms my age is {self.my_age} "
    def get_grans_age():
        return super().get_age
    
class Child(Mother):
    def __init__(self ,my_name,name):
        super().__init__(name)
        self.my_name = my_name
    def message(self):
        return f"My name is {self.my_name} and my mom is {self.name}"
my_grans = Granny(56,"Sophie")
print(my_grans.message())
my_moms = Mother(2,45 , "Manki",78)
print(my_moms.message())
# me = Child("Abongile" , "Sibongile")
# print(me.message())
print("My moms age is " + str(my_moms.get_age()))


###### Why would we want to use object oriented programming
