class Book:
    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name

    def __repr__(self):
        return f"Book ID : {self.book_id} | Book Title : {self.book_name}"
   
class Library:
    book_list = []

    def entry_book(self, book):
        self.book_list.append(book)


books = Library()
book1 = Book(1, "Prince")
book2 = Book(2, "Fault")

books.entry_book(book1)
books.entry_book(book2)

print(book1)
print(book2)
print(books.book_list)