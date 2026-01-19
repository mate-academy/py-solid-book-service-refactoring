import json

from app.interfaces import (
    PrinterInterface,
    SerializerInterface,
    DisplayInterface,
    DisplayType, PrintType, SerializeType
)
import xml.etree.ElementTree as Etree

from app.models import Book


class Display(DisplayInterface):
    def display(self, book: Book, display_type: DisplayType) -> None:
        if display_type == DisplayType.CONSOLE:
            return self.display_console(book)
        elif display_type == DisplayType.REVERSE:
            return self.display_reverse(book)

        raise ValueError(f"Unknown display type: {display_type}")

    def display_console(self, book: Book) -> None:
        print(book.content)

    def display_reverse(self, book: Book) -> None:
        print(book.content[::-1])


class Printer(PrinterInterface):
    def print_book(self, book: Book, print_type: PrintType) -> None:
        if print_type == PrintType.CONSOLE:
            return self.print_console(book)
        elif print_type == PrintType.REVERSE:
            return self.print_reverse(book)

        raise ValueError(f"Unknown print type: {print_type}")

    def print_console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n"
              f"{book.content}")

    def print_reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...\n"
              f"{book.content[::-1]}")


class Serializer(SerializerInterface):
    def serialize(self, book: Book, serialize_type: SerializeType) -> str:
        if serialize_type == SerializeType.JSON:
            return self.serialize_json(book)
        elif serialize_type == SerializeType.XML:
            return self.serialize_xml(book)

        raise ValueError(f"Unknown serialize type: {serialize_type}")

    def serialize_json(self, book: Book) -> json:
        return json.dumps({"title": book.title, "content": book.content})

    def serialize_xml(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content

        return Etree.tostring(root, encoding="unicode")
