import json
from app import app

def test_view_books():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200

def test_add_book():
    client = app.test_client()
    new_book = {"title": "Clean Code", "author": "Robert C. Martin"}
    response = client.post("/books", data=json.dumps(new_book), content_type="application/json")
    assert response.status_code == 201

def test_issue_book():
    client = app.test_client()
    response = client.post("/books/issue/1")
    assert response.status_code == 200
    assert "issued successfully" in response.json["message"]
