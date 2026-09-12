import json
from xml.etree import ElementTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class ConsoleDisplayer:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerializer:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")

        title = ElementTree.SubElement(root, "title")
        title.text = book.title

        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displayers[method_type].display(book)
        elif cmd == "print":
            printers[method_type].print_book(book)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book)
