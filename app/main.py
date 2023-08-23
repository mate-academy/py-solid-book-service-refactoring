import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Serialize(ABC):
    @abstractmethod
    def serialize_book(self, book: Book) -> None:
        pass


class Display(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display_book(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeToJSON(Serialize):
    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeToXML(Serialize):
    def serialize_book(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": DisplayConsole(), "reverse": DisplayReverse()
    }
    printers = {
        "console": PrintConsole(), "reverse": PrintReverse()
    }
    serializers = {
        "json": SerializeToJSON(), "xml": SerializeToXML()
    }
    for cmd, method_type in commands:
        if cmd == "display":
            display = displays.get(method_type)
            return display.display_book(book)
        elif cmd == "print":
            printer = printers.get(method_type)
            return printer.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            return serializer.serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
