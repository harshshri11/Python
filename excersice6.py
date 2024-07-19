class Library:
    def __init__(self):
        self.no_of_books = 0
        self.book_title = []
    def add_book(self,book_title):
        self.book_title.append(book_title)
        self.no_of_book =len(self.book_title)
        self.no_of_books += 1

    def print_book(self):
        print(f"books in the  labrary are {self.no_of_books} are books are")
        for book_title in  self.book_title:
          print(book_title)


lab = Library()
lab.add_book("harry potter")
lab.add_book("agnipankh")
lab.print_book()

