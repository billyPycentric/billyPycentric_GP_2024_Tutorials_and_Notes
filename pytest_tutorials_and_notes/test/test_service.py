import pytest
import source.service as service
import unittest.mock as mock

# write a test to get user from db
#use decorater mock.patch("path")
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(any_var):
    any_var.return_value = "Two"
    user_name = service.get_user_from_db(2)

    assert user_name == "Two"  