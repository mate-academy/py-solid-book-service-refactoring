from abc import ABC, abstractmethod


class PrintBook(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class PrintBookReverse(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


BOOK_PRINT_PROCESSORS = {
    "console": PrintBookConsole,
    "reverse": PrintBookReverse,
}
