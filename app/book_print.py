from app.book import Book


class BookPrint:
    def __init__(self, book: Book) -> None:
        self.book = book

    def console(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def reverse(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
