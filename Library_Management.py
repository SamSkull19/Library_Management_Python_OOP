class Library:
    book_list = []

    def entry_book(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name
        self.book_list.append([self.book_id, self.book_name])


books = Library()

books.entry_book(121, 'Harry Potter')
books.entry_book(174, 'Dune')
print(books.book_list)