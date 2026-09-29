# Library Management System

## Introduction

This project is a simple **Library Management System** developed using Python. It allows the user to manage books and library members through a menu-driven program.

The project uses **List and Dictionary** data structures for storing information and the **Pickle module** for permanent data storage.

## Features

* Add a new book
* Display all books
* Search for a book
* Add a new library member
* Display all members
* Issue a book to a member
* Return a book
* Remove a book
* Save data permanently
* Automatically load previously saved data

## Project Structure

```text
Library Management System
│
├── main.py
├── library.py
├── data.py
├── library.dat
└── README.md
```

## Modules

### 1. main.py

This is the main program file. It displays the menu and calls the required functions from the `library.py` and `data.py` modules.

### 2. library.py

This module contains the main library functions such as:

* Adding books
* Displaying books
* Searching books
* Adding members
* Displaying members
* Issuing books
* Returning books
* Removing books

### 3. data.py

This module handles data storage using the **Pickle** module.

It contains two main functions:

* `load_data()` – Loads previously saved data.
* `save_data()` – Saves the current data into `library.dat`.

## Data Structures Used

### List

Books are stored using a list.

```python
books = []
```

Each book is represented using a dictionary.

```python
{
    "id": 101,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "status": "Available",
    "issued_to": None
}
```

### Dictionary

Members are stored using a dictionary.

```python
members = {}
```

Each member contains their name and the list of books issued to them.

```python
{
    1: {
        "name": "Rahul",
        "issued_books": [101]
    }
}
```

## File Handling

The project uses the `pickle` module to store data permanently.

```python
pickle.dump(books, file)
pickle.dump(members, file)
```

The saved data can be loaded again using:

```python
books = pickle.load(file)
members = pickle.load(file)
```

The data is stored in a file named:

```text
library.dat
```

## How to Run

1. Keep all the Python files in the same folder.
2. Open the folder in Python IDLE, VS Code, or another Python IDE.
3. Run `main.py`.
4. Select the required option from the menu.
5. The data will automatically be saved in `library.dat`.

## Requirements

* Python 3.x
* No external libraries are required.
* The built-in `pickle` and `os` modules are used.

## Menu

```text
======================================
       LIBRARY MANAGEMENT SYSTEM
======================================
1. Add Book
2. Display Books
3. Search Book
4. Add Member
5. Display Members
6. Issue Book
7. Return Book
8. Remove Book
9. Save Data
10. Exit
======================================
```

## Conclusion

The Library Management System demonstrates the use of **Python functions, modules, lists, dictionaries, file handling, and the Pickle module** to create a basic library management application with permanent data storage.
