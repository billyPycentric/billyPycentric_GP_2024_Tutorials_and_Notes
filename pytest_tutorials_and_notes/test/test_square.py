import pytest
import source.shapes as shapes


# trying parametirizing
@pytest.mark.parametrize("side_length,expected_area",[(2,4),(4,16),(9,81)])
def test_multiple_squares(side_length , expected_area):
    assert shapes.Square(side_length).area() == expected_area

# Now testing for perimeter
@pytest.mark.parametrize("side_length ,expected_perimeter" , [(2,8),(1,4)])
def test_multiple_perimeters(side_length , expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter