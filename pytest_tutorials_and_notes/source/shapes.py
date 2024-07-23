import math

class Shape:
    
    def area(self):
        pass
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi *self.radius    

## My Own Shape that extends shapes    
class Rectangle(Shape):
    def __init__(self ,first_pair,second_pair):
        self.first_pair = first_pair
        self.second_pair = second_pair

    def area(self):
        return self.first_pair * self.second_pair

    def perimeter(self):
        return 2*self.first_pair + 2*self.second_pair    
    
## Testing out a rhombus for test by func

class Rhombus(Shape):
    # initialize the shape
    def __init__(self , length , width):
        self.length = length
        self.width = width

    # Now the area and the perimeter
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length*2) + (self.width * 2)
    

class Square(Rectangle):
    def __init__(self, first_pair):
        super().__init__(first_pair, first_pair)