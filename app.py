import json
import streamlit as st

FILENAME = 'data.json'

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            st.success("Data loaded successfully")
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        st.success("Data saved successfully")

def add_book(data):
    title = st.text_input("Enter the title: ").strip()
    author = st.text_input("Enter the author: ").strip()
    year = st.number_input("Enter the year: ", min_value=0, step=1)
    genre = st.text_input("Enter the genre: ").strip()
    read = st.radio("Have you read the book?", ('Yes', 'No')).strip().lower()
    status_read = read == 'yes'
    
    if st.button("Add Book"):
        if title and author and genre:
            book = {
                'title': title,
                'author': author,
                'year': year,
                'genre': genre,
                'read': status_read
            }
            data.append(book)
            save_data(FILENAME, data)
            st.success("Book added successfully")
        else:
            st.error("Please fill in all required fields (Title, Author, Genre)")

def remove_book(data):
    title = st.text_input("Enter the title of the book to remove: ").strip()
    if st.button("Remove Book"):
        initial_length = len(data)
        data[:] = [book for book in data if book['title'].lower() != title.lower()]
        if len(data) < initial_length:
            save_data(FILENAME, data)
            st.success("Book removed successfully")
        else:
            st.error("Book not found")

def search_book(data):
    search_by = st.radio("Search by:", ('Title', 'Author'))
    query = st.text_input("Enter the title or author: ").strip().lower()
    if st.button("Search"):
        matches = []
        for book in data:
            if search_by == 'Title':
                if query in book['title'].lower():
                    matches.append(book)
            else:
                if query in book['author'].lower():
                    matches.append(book)
        if matches:
            for match in matches:
                st.write(f"Title: {match['title']}")
                st.write(f"Author: {match['author']}")
                st.write(f"Year: {match['year']}")
                st.write(f"Genre: {match['genre']}")
                st.write(f"Read: {'Yes' if match['read'] else 'No'}")
                st.write("---")
        else:
            st.error("No books found")

def display_books(data):
    if data:
        for book in data:
            st.write(f"Title: {book['title']}")
            st.write(f"Author: {book['author']}")
            st.write(f"Year: {book['year']}")
            st.write(f"Genre: {book['genre']}")
            st.write(f"Read: {'Yes' if book['read'] else 'No'}")
            st.write("---")
    else:
        st.warning("No books to display")

def display_statistics(data):
    total_books = len(data)
    total_read = len([book for book in data if book['read']])
    total_unread = total_books - total_read
    st.write(f"Total books: {total_books}")
    st.write(f"Total read: {total_read}")
    st.write(f"Total unread: {total_unread}")

def main():
    st.title("Personal Library Manager")
    data = load_data(FILENAME)
    
    menu = ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Add a book":
        add_book(data)
    elif choice == "Remove a book":
        remove_book(data)
    elif choice == "Search for a book":
        search_book(data)
    elif choice == "Display all books":
        display_books(data)
    elif choice == "Display statistics":
        display_statistics(data)
    elif choice == "Exit":
        save_data(FILENAME, data)
        st.write("Exiting...")

if __name__ == '__main__':
    main()
