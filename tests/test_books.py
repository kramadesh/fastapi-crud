def test_create_book(test_client):
    response = test_client.post(
        "/books/",
        json={"title": "Great Expectations", "author": "Charles Dickens"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Great Expectations"
    assert data["author"] == "Charles Dickens"
    assert "id" in data


def test_read_books(test_client):
    response = test_client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # at least one book exists


def test_read_book_by_id(test_client):
    # First create
    create_resp = test_client.post(
        "/books/", json={"title": "Clean Code", "author": "Robert Martin"}
    )
    book_id = create_resp.json()["id"]

    # Then fetch
    response = test_client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == "Clean Code"


def test_update_book(test_client):
    # Create
    create_resp = test_client.post(
        "/books/", json={"title": "Old Title", "author": "Author X"}
    )
    book_id = create_resp.json()["id"]

    # Update
    response = test_client.put(
        f"/books/{book_id}", json={"title": "New Title", "author": "Author X"}
    )
    assert response.status_code == 200
    data = response.json()
    print(f"data = {data}")
    assert data["title"] == "New Title"


def test_delete_book(test_client):
    # Create
    create_resp = test_client.post(
        "/books/", json={"title": "To Delete", "author": "Author Y"}
    )
    book_id = create_resp.json()["id"]

    # Delete
    response = test_client.delete(f"/books/{book_id}")
    assert response.status_code == 200

    # Verify deletion
    response = test_client.get(f"/books/{book_id}")
    assert response.status_code == 404
