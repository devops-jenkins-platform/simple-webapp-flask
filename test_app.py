from app import app


def test_main():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome!"


def test_how_are_you():
    client = app.test_client()
    response = client.get("/how-are-you")
    assert response.status_code == 200
    assert response.data == b"I am good, how about you?"
