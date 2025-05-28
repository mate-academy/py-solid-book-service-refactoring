from abc import ABC, abstractmethod


class PrintType(ABC):

    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class PrintConsoleType(PrintType):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintDisplayType(PrintType):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
