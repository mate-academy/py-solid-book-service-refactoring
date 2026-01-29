from app.contracts import BookProtocol
from app.display.base import Displayer


class ConsoleDisplayer(Displayer):
    def display(self, book: BookProtocol) -> None:
        print(book.content)
