class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books =[]

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
    
    def get_no_of_books(self):
          return self.no_of_books
    
    def print_all_books(self):
         for book in self.books:
              print(book)


my_library = Library()
my_library.add_book('Harry potter')
my_library.add_book('13 reason why?')
my_library.add_book('fault in my star')

print("Number of books:", my_library.get_no_of_books())
my_library.print_all_books()
