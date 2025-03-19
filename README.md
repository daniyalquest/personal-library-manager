# Personal Library Manager

The Personal Library Manager is a Streamlit-based application that allows users to manage their personal book collection. Users can add, remove, search, and display books, as well as view statistics about their collection.

## Features

- **Add a Book**: Add a new book to your collection by providing the title, author, year, genre, and read status.
- **Remove a Book**: Remove a book from your collection by entering its title.
- **Search for a Book**: Search for books in your collection by title or author.
- **Display All Books**: Display all books in your collection with their details.
- **Display Statistics**: View statistics about your collection, including the total number of books, the number of books read, and the number of books unread.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/personal-library-manager.git
    ```
2. Navigate to the project directory:
    ```sh
    cd personal-library-manager
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to access the application.

## File Structure

- `app.py`: The main application file containing the Streamlit code.
- `data.json`: The JSON file where the book data is stored.
- `requirements.txt`: The file containing the list of dependencies.