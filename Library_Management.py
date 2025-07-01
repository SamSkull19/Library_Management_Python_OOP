class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability


    def __repr__(self):
        return f"Book ID : {self.book_id} | Book Title : {self.title} | Book Author : {self.author} | Book Availability : {self.availability}"
   
class Library:
    book_list = []

    def entry_book(self, book):
        self.book_list.append(book)


books = Library()
book1 = Book(2, "Mockingbird", "Harper", False)
book2 = Book(3, "Gatsby", "Fitzgerald", True)

books.entry_book(book1)
books.entry_book(book2)

print(book1)
print(book2)
print(books.book_list)