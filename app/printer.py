from app.book import Book
from app.display import DisplayStrategy


class Printer:
    def print(self, display: DisplayStrategy, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        display.display(book.content)
