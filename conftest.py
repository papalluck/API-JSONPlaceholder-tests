import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_data():
    return {
        "userId": 1,
        "title": "Тестовый заголовок поста",
        "body": "Тестовое тело поста"
    }