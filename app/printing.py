from abc import ABC


class BookPrint(ABC):
    def print(self, title: str, content: str) -> None:
        raise ValueError("Unknown print type")


class BookPrintConsole(BookPrint):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class BookPrintReverse(BookPrint):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
