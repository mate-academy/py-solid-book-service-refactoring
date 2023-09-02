from abc import ABC, abstractmethod


class BookPrinter(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class ConsoleBookPrinter(BookPrinter):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReverseBookPrinter(BookPrinter):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
