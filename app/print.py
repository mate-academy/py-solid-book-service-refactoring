from abc import abstractmethod, ABC

from app.solid import Book, Formatter


class Printer(ABC):
    def __init__(self, book: Book, formatter: Formatter) -> None:
        self.book = book
        self.formatter = formatter

    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, book: Book, formatter: Formatter) -> None:
        super().__init__(book, formatter)

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.formatter.format(self.book.content))


class ReversePrinter(Printer):
    def __init__(self, book: Book, formatter: Formatter) -> None:
        super().__init__(book, formatter)

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.formatter.format(self.book.content))
