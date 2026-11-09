import json
import xml.etree.ElementTree as ET  # noqa: N817
from dataclasses import dataclass
from typing import Type


@dataclass
class Book:
    title: str
    content: str


class ConsoleDisplay():
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay():
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrinter():
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}... {book.content}")


class ReversePrinter():
    def print_book(self, book: Book) -> None:
        print(f"Book in reverse {book.title}... {book.content[::-1]}")


class JsonSerializer():
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer():
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


DISPLAY_HANDLERS: dict[str, Type[object]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_HANDLERS: dict[str, Type[object]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_HANDLERS: dict[str, Type[object]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display":
            return DISPLAY_HANDLERS[method_type]().display(book.content)

        elif cmd == "print":
            return PRINT_HANDLERS[method_type]().print_book(book)

        elif cmd == "serialize":
            return SERIALIZER_HANDLERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
