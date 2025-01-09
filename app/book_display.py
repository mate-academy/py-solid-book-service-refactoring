from app.book import Book
from app.command_execute import CommandExecute


class BookDisplayConsole(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.book = book

    def execute(self) -> None:
        print(self.book.content)


class BookDisplayReverse(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.book = book

    def execute(self) -> None:
        print(self.book.content[::-1])
