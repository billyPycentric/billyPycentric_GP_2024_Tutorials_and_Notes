## using this test file for TEST by FUNCTION
import pytest
#import source.shapes as shapes


def test_area(my_rhombus):
    
    assert my_rhombus.area() == 4*6

# Testing the perimeter
def test_perimeter(my_rhombus):
    assert my_rhombus.perimeter() == (2*4) + (2*6)
