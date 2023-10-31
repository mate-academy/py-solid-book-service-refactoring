from abc import ABC, abstractmethod


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrintBook(PrintBook):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintBook(PrintBook):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
