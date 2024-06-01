# Book-Dictionary API

Welcome to the Book-Dictionary API repository. This project is built using FastAPI and allows you to perform CRUD (Create, Read, Update, Delete) operations on a collection of books. 

## Features

- **Create**: Add a new book to the dictionary.
- **Read**: Retrieve details of a book or list all books.
- **Update**: Modify details of an existing book.
- **Delete**: Remove a book from the dictionary.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alihassanml/Book-Dictionary.git
   cd Book-Dictionary
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000`. You will see the API documentation provided by Swagger UI at `http://127.0.0.1:8000/docs`.

## Usage

### API Endpoints

Here are the main endpoints you can interact with:

- **GET** `/books/` - Retrieve a list of all books.
- **GET** `/books/{book_id}` - Retrieve details of a specific book by ID.
- **POST** `/books/` - Add a new book.
  - Example payload:
    ```json
    {
      "title": "Book Title",
      "author": "Author Name",
      "summary": "Book Summary",
      "isbn": "123-4567890123"
    }
    ```
- **PUT** `/books/{book_id}` - Update an existing book by ID.
  - Example payload:
    ```json
    {
      "title": "Updated Book Title",
      "author": "Updated Author Name",
      "summary": "Updated Book Summary",
      "isbn": "123-4567890123"
    }
    ```
- **DELETE** `/books/{book_id}` - Delete a book by ID.

### Example Requests

- **Create a new book:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/books/" -H "Content-Type: application/json" -d '{"title": "New Book", "author": "John Doe", "summary": "An interesting book.", "isbn": "123-4567890123"}'
  ```

- **Get all books:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/books/"
  ```

- **Get a book by ID:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/books/1"
  ```

- **Update a book:**
  ```bash
  curl -X PUT "http://127.0.0.1:8000/books/1" -H "Content-Type: application/json" -d '{"title": "Updated Book", "author": "Jane Doe", "summary": "An updated interesting book.", "isbn": "123-4567890123"}'
  ```

- **Delete a book:**
  ```bash
  curl -X DELETE "http://127.0.0.1:8000/books/1"
  ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive guide to setting up, running, and using the Book-Dictionary API, making it easier for contributors and users to get started.
