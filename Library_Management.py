class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"{self._title} has been borrowed.")
       
        else:
            print(f"{self._title} is already borrowed and not available.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"{self._title} has been returned.")
       
        else:
            print(f"{self._title} is already available and not borrowed.")

    def view_book_info(self):
        return f"Book ID : {self.__book_id} | Book Title : {self._title} | Book Author : {self._author} | Book Availability : {self.__availability}"

    def __repr__(self):
        return f"Book ID : {self.book_id} | Book Title : {self.title} | Book Author : {self.author} | Book Availability : {self.availability}"
   

class Library:
    book_list = []

    def entry_book(self, book):
        self.book_list.append(book)

    def get_book_by_id(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                return book
        return None
    

books = Library()
book1 = Book(1, "1984", "Orwell", True)
book2 = Book(2, "Mockingbird", "Harper", False)
book3 = Book(3, "Gatsby", "Fitzgerald", True)
book4 = Book(4, "Florence", "Gerald", True)
book5 = Book(5, "Franco", "Issac", False)
book6 = Book(6, "Jungle", "James", True)
book7 = Book(7, "Trunk", "Mary", True)
book8 = Book(8, "House", "Carl", False)

books.entry_book(book1)
books.entry_book(book2)
books.entry_book(book3)
books.entry_book(book4)
books.entry_book(book5)
books.entry_book(book6)
books.entry_book(book7)
books.entry_book(book8)

def borrow_book(book_id):
    book = books.get_book_by_id(book_id)
   
    if book:
        book.borrow_book()
    else:
        print(f"Error: Book ID {book_id} not found.")

def return_book(book_id):
    book = books.get_book_by_id(book_id)
   
    if book:
        book.return_book()
    else:
        print(f"Error: Book ID {book_id} not found.")

def view_book_info():
    for book in Library.book_list:
        print(book.view_book_info())

        
print(books.book_list)

for book in books.book_list:
    print(book)