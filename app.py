from flask import Flask, jsonify, request

app = Flask(__name__)
books_db = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "available": True} ]

@app.route("/books", methods=["GET"])
def view_books():
    return jsonify({"status": "success", "books": books_db}), 200

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"status": "error", "message": "Missing title or author"}), 400
    
    new_book = {
        "id": len(books_db) + 1,
        "title": data["title"],
        "author": data["author"],
        "available": True
    }
    books_db.append(new_book)
    return jsonify({"status": "success", "message": "Book added successfully", "book": new_book}), 201

@app.route("/books/issue/<int:book_id>", methods=["POST"])
def issue_book(book_id):
    for book in books_db:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return jsonify({"status": "success", "message": f"Book '{book['title']}' issued successfully"}), 200
            else:
                return jsonify({"status": "error", "message": "Book is already issued"}), 400
                
    return jsonify({"status": "error", "message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
