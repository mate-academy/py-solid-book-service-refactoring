from app.book import Book
from app.interfaces import Display, ShowBookDetail


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ShowConsoleBookDetail(ShowBookDetail):
    def show(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ShowReverseBookDetail(ShowBookDetail):
    def show(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
