import pytest
import source.functions as functions

def test_add():
    result = functions.add(1,5)
    assert result == 6

# adding strings

def test_add_strings():
    result = functions.add("my name is " , "Billy")
    assert result == "my name is Billy"

# testing divide for denominator = 0
def test_divideByZero():
    with pytest.raises(ValueError):
        functions.divide(1,0)

# testing divide
def test_divide():
    result = functions.divide(6,2)
    assert result == 3
