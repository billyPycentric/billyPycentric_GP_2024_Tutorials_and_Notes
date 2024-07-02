import pytest , math
import source.shapes as shapes

class TestCircle:
    
    # Setting up a method
    def setup_method(self , method):
        print(f"Setting up the {method}")
        self.circle = shapes.Circle(10)
        
    # Setting up a method
    def teardown_metho(self , method):
        print(f"Tearing downn the {method}")
        del self.circle


    def test_one(self):
        assert True

    def test_area(self):
        result = self.circle.area()
        expected = math.pi * self.circle.radius**2
        assert result == expected

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = self.circle.radius * 2*math.pi
        assert result == expected    