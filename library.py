from data import save_library


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid integer.")


def add_book(books, members):
    book_id = read_int("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": None
    }

    books.append(book)
    save_library(books, members)

    print("Book added successfully!")


def display_books(books):
    if not books:
        print("No books available in the library.")
        return

    print("Books in the Library:")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")


def search_book(books):
    book_id = read_int("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print(f"Book Found: ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            return

    print("Book not found!")


def add_member(books, members):
    member_id = read_int("Enter Member ID: ")

    for member in members:
        if member["id"] == member_id:
            print("Member ID already exists!")
            return

    name = input("Enter Member Name: ").strip()
    if not name:
        print("Member name cannot be empty.")
        return

    member = {
        "id": member_id,
        "name": name
    }

    members.append(member)
    save_library(books, members)

    print("Member added successfully!")


def display_members(members):
    if not members:
        print("No members registered in the library.")
        return

    print("Library Members:")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}")


def issue_book(books, members):
    book_id = read_int("Enter Book ID to issue: ")
    member_id = read_int("Enter Member ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                for member in members:
                    if member["id"] == member_id:
                        book["status"] = "Issued"
                        book["issued_to"] = member_id
                        save_library(books, members)
                        print(f"Book ID {book_id} issued to Member ID {member_id}.")
                        return
                print("Member not found!")
                return
            else:
                print("Book is already issued!")
                return

    print("Book not found!")


def return_book(books, members):
    book_id = read_int("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                book["issued_to"] = None
                save_library(books, members)
                print(f"Book ID {book_id} returned successfully.")
                return
            else:
                print("Book is not issued!")
                return

    print("Book not found!")


def remove_book(books, members):
    book_id = read_int("Enter Book ID to remove: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_library(books, members)
            print(f"Book ID {book_id} removed successfully.")
            return

    print("Book not found!")