import json
import xml.etree.ElementTree as ElT
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayProceed:
    display_types = {
        "console": ConsoleBookDisplay,
        "reverse": ReverseBookDisplay}

    def display_book(self, display_type: str, book: Book) -> str:
        if display_type in self.display_types:
            return self.display_types[display_type]().display(book)
        raise ValueError(f"Unknown display type: {display_type}")


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrinterProceed:
    printers = {"console": ConsolePrinter, "reverse": ReversePrinter}

    def go_print(self, print_type: str, book: Book) -> str:
        if print_type in self.printers:
            return self.printers[print_type]().print_book(book)
        raise ValueError(f"Unknown print type: {print_type}")


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")


class SerializerProceed:
    serialize_types = {"json": JSONSerializer, "xml": XMLSerializer}

    def serialize_book(self, serialize_type: str, book: Book) -> str:
        if serialize_type in self.serialize_types:
            return self.serialize_types[serialize_type]().serialize(book)
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_printer = PrinterProceed()
    book_displayer = DisplayProceed()
    book_serializer = SerializerProceed()
    for cmd, method_type in commands:
        if cmd == "display":
            book_displayer.display_book(method_type, book)
        elif cmd == "print":
            book_printer.go_print(method_type, book)
        elif cmd == "serialize":
            return book_serializer.serialize_book(method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "console"), ("serialize", "xml")]))
