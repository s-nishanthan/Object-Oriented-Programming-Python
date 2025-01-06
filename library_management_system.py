class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed the book: '{self.title}'")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned the book: '{self.title}'")
        else:
            print(f"The book '{self.title}' was not borrowed.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print(f"{self.name} already borrowed the book '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"{self.name} did not borrow the book '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Main function to interact with the Library System
def main():
    # Creating books and members
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1)
    book2 = Book("1984", "George Orwell", 2)
    
    member1 = Member("Alice", 101)
    member2 = Member("Bob", 102)
    
    # Simulate library operations
    member1.borrow_book(book1)
    member1.list_borrowed_books()
    
    member2.borrow_book(book1)  # Trying to borrow the same book
    member1.return_book(book1)
    member2.borrow_book(book1)  # Now Bob can borrow it

    member2.list_borrowed_books()

if __name__ == "__main__":
    main()
