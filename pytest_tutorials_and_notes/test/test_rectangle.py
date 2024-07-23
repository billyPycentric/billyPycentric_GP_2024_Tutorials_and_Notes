import pytest
import source.shapes as shapes

class TestRectangle:

    def setup_method(self , method):
        print(f"setting up {method}")
        self.rectangle = shapes.Rectangle(2,3)

    def teardown_method(self, method):
        print(f"tearing down {method}")
        del self.rectangle

    def test_area(self):
        result = self.rectangle.area()
        expected = self.rectangle.first_pair * self.rectangle.second_pair
        assert result == expected    

    def test_perimeter(self):
        result = self.rectangle.perimeter()
        expected = self.rectangle.first_pair*2 + self.rectangle.second_pair*2
        assert result == expected
