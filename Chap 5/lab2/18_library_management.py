# Library Management System

class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = {
            "title": title,
            "issued": False
        }

        print("Book added successfully")

    def display_books(self):
        if not self.books:
            print("No books available")
            return

        for book_id, book in self.books.items():
            status = "Issued" if book["issued"] else "Available"

            print(book_id, "-", book["title"], "-", status)

    def issue_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = True
                print("Book issued successfully")
            else:
                print("Book is already issued")
        else:
            print("Book not found")

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = False
                print("Book returned successfully")
            else:
                print("Book was not issued")
        else:
            print("Book not found")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")

        library.add_book(book_id, title)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book_id = input("Enter book ID: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Enter book ID: ")
        library.return_book(book_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice")