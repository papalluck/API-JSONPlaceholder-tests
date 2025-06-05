import pytest
import requests
from conftest import BASE_URL, post_data


def test_update_post_success(post_data):
    create_response = requests.post(f"{BASE_URL}/posts", json=post_data)
    assert create_response.status_code == 201
    created_post = create_response.json()
    post_id = created_post["id"]

    updated_post_data = {
        "title": "foo"
    }

    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=updated_post_data)
    assert response.status_code == 200
    response_data = response.json()

    assert response_data["title"] == updated_post_data["title"]