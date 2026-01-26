from app.models import Book
from app.interfaces import ActionInterface


class ConsoleDisplay(ActionInterface):
    def execute(self, book: Book) -> None:
        print(f"[Display] {book.content}")


class ReverseDisplay(ActionInterface):
    def execute(self, book: Book) -> None:
        print(f"[Display Reverse] {book.content[::-1]}")
