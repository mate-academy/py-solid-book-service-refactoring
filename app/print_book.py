from app.book import Book


class PrintBook:

    def __init__(self, book: Book) -> None:
        self.book = book

    def console(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
