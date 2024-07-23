import pytest
import source.shapes as shapes

@pytest.fixture
def my_rhombus():
    return shapes.Rhombus(4,6)