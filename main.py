from data import load_library, save_library
from library import add_book, display_books, display_members, issue_book, remove_book, return_book, search_book, add_member

books, members = load_library()

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. Display Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Remove Book")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number from 1 to 9.")
        continue

    if choice == 1:
        add_book(books, members)
    elif choice == 2:
        display_books(books)
    elif choice == 3:
        search_book(books)
    elif choice == 4:
        add_member(books, members)
    elif choice == 5:
        display_members(members)
    elif choice == 6:
        issue_book(books, members)
    elif choice == 7:
        return_book(books, members)
    elif choice == 8:
        remove_book(books, members)
    elif choice == 9:
        save_library(books, members)
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 9.")