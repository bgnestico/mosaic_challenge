from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def load_books_from_file():
    with open('data/books.json', 'r') as file:
        return json.load(file)


def save_books_to_file(books):
    with open('data/books.json', 'w') as file:
        json.dump(books, file, indent=4)


@app.route('/books', methods=['GET'])
def get_books():
    books = load_books_from_file()
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    books = load_books_from_file()
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    books = load_books_from_file()
    books.append(data)
    save_books_to_file(books)
    return jsonify({'message': 'Book created'}), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    books = load_books_from_file()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books[i] = data
            save_books_to_file(books)
            return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = load_books_from_file()
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            save_books_to_file(books)
            return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404
