import pytest
import requests
from conftest import BASE_URL, post_data


def test_create_post_success(post_data):
    response = requests.post(f"{BASE_URL}/posts", json=post_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["userId"] == post_data["userId"]
    assert response_data["title"] == post_data["title"]
    assert response_data["body"] == post_data["body"]
    assert "id" in response_data