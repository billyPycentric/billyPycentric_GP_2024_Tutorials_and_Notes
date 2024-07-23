### Blue prints for creating something

class Vehicle():
    # def __init__(self ,make,model):
    #     self.make = make
    #     self.model = model
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def moves(sel2):
        print("it moves")
    def get_model(self):
        return self.model

my_car = Vehicle("telsa " , "M4")  
print(str((my_car.moves())) + " and here is the car " + my_car.get_model())
# print(type(my_car.  moves()))