import pytest
import requests
from conftest import BASE_URL, post_data

def test_delete_post_success(post_data):

    create_response = requests.post(f"{BASE_URL}/posts", json=post_data)
    assert create_response.status_code == 201
    created_post = create_response.json()
    post_id = created_post["id"]
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
