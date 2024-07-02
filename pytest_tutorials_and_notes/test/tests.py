import pytest
import source.functions as functions

def test_add():
    result = functions.add(1,5)
    assert result == 6