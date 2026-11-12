from app.models import Book
from app.strategies.output import OutputStrategy


class BookPrinter:
    @staticmethod
    def display(book: Book, strategy: OutputStrategy) -> None:
        print(strategy.render(book.content))

    @staticmethod
    def print_book(book: Book, strategy: OutputStrategy) -> None:
        print(f"Printing the book: {book.title}...")
        print(strategy.render(book.content))
