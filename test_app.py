import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    with app.test_client() as client:
        yield client

def test_home_redirects_to_login(client):
    response = client.get("/")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

def test_login_success(client):
    response = client.post("/login", data={"username": "admin", "password": "password123"}, follow_redirects=True)
    assert b"Welcome, admin" in response.data

def test_login_failure(client):
    response = client.post("/login", data={"username": "wrong", "password": "wrong"}, follow_redirects=True)
    assert b"Invalid credentials" in response.data

def test_welcome_requires_login(client):
    response = client.get("/welcome", follow_redirects=True)
    assert b"Login Page" in response.data

def test_logout(client):
    # First login
    client.post("/login", data={"username": "admin", "password": "password123"}, follow_redirects=True)
    # Then logout
    response = client.get("/logout", follow_redirects=True)
    assert b"Login Page" in response.data
