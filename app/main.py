import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book, display_type: str) -> None:
        pass


class DisplayConsoleProcessor(BookDisplay):
    def display(self, book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)


class DisplayReverseProcessor(BookDisplay):
    def display(self, book: Book, display_type: str) -> None:
        if display_type == "reverse":
            print(book.content[::-1])


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book, print_type: str) -> None:
        pass


class PrinterConsoleProcessor(BookPrinter):

    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)


class PrinterReverseProcessor(BookPrinter):
    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book, serialize_type: str) -> str:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


class SerializerJson(BookSerializer):
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(BookSerializer):
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")


# class SerializerHandler(SerializerJson, SerializerXML)
def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_processors = {
        "console": DisplayConsoleProcessor(),
        "reverse": DisplayReverseProcessor(),
    }

    printer_processors = {
        "console": PrinterConsoleProcessor(),
        "reverse": PrinterReverseProcessor(),
    }

    serializer_processors = {
        "json": SerializerJson(),
        "xml": SerializerXML(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_processor = display_processors.get(method_type)
            if display_processor:
                display_processor.display(book, method_type)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            printer_processor = printer_processors.get(method_type)
            if printer_processor:
                printer_processor.print_book(book, method_type)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serializer_processor = serializer_processors.get(method_type)
            if serializer_processor:
                return serializer_processor.serialize(book, method_type)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
