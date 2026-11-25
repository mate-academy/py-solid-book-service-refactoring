import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BookDisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class BookDisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Printer(ABC):
    @abstractmethod
    def printer(self, book: Book) -> None:
        pass


class BookPrintConsole(Printer):
    def printer(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookPrintReverse(Printer):
    def printer(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


DISPLAY = {"console": BookDisplayConsole, "reverse": BookDisplayReverse}
PRINTER = {"console": BookPrintConsole, "reverse": BookPrintReverse}
SERIALIZE = {"json": SerializeJson, "xml": SerializeXml}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY[method_type]().display(book)
        elif cmd == "print":
            PRINTER[method_type]().printer(book)
        elif cmd == "serialize":
            return SERIALIZE[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
