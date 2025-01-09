from app.book import Book
from app.command_execute import CommandExecute


class BookPrintConsole(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def execute(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class BookPrintReverse(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def execute(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
