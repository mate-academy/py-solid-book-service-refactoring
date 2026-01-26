from app.interfaces import ActionInterface
from app.models import Book


class ConsolePrint(ActionInterface):
    def execute(self, book: Book) -> None:
        print(f"Printing: {book.title}...\n{book.content}")


class ReversePrint(ActionInterface):
    def execute(self, book: Book) -> None:
        print(f"Printing Reverse: {book.title}...\n{book.content[::-1]}")
