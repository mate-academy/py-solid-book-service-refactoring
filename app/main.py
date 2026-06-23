import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IBookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class IBookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class IBookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    ReverseDisplay().display(sample_book)
    print(XmlSerializer().serialize(sample_book))


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_map = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    print_map = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serialize_map = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_map[method_type].display(book)
        elif cmd == "print":
            print_map[method_type].print_book(book)
        elif cmd == "serialize":
            return serialize_map[method_type].serialize(book)
