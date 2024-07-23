import pytest
import source.service as service
import unittest.mock as mock
import requests


# write a test to get user from db
#use decorater mock.patch("path")
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(any_var):
    any_var.return_value = "Two"
    user_name = service.get_user_from_db(2)

    assert user_name == "Two"  

@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_reponse = mock.Mock()
    mock_reponse.status_code = 200
    mock_reponse.json.return_value = {"id" : 1,"name" : "John Doe"}
    mock_get.return_value = mock_reponse
    data = service.get_user()
    
    assert data == mock_reponse.json.return_value

@mock.patch("requests.get")
def test_get_comments(any_var):
    mock_res = mock.Mock()
    mock_res.status_code = 200
    mock_res.json.return_value = {"postId": 1,"id": 1,}
    any_var.return_value = mock_res
    data = service.get_comments()

    assert data == mock_res.json.return_value