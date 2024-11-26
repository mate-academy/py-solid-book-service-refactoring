from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ConsoleReverse(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintConsole(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
