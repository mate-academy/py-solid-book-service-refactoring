from app.book import Book
from app.formatter import Formatter


class BookPrinter:
    def print_book(self, book: Book, formatter: Formatter) -> None:
        print(f"Printing the book: {book.title}...")
        formatted_content = formatter.format(book)
        print(formatted_content)
