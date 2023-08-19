from abc import ABC, abstractmethod


class PrintManager(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class PrintConsole(PrintManager):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintReverse(PrintManager):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
