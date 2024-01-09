import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsoleProcessor(BookDisplay):
    def __init__(self, display_type: str) -> None:
        self.display_type = display_type

    def display(self, book: Book) -> None:
        if self.display_type == "console":
            print(book.content)


class DisplayReverseProcessor(BookDisplay):
    def __init__(self, display_type: str) -> None:
        self.display_type = display_type

    def display(self, book: Book) -> None:
        if self.display_type == "reverse":
            print(book.content[::-1])


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrinterConsoleProcessor(BookPrinter):
    def __init__(self, print_type: str) -> None:
        self.print_type = print_type

    def print_book(self, book: Book) -> None:
        if self.print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)


class PrinterReverseProcessor(BookPrinter):
    def __init__(self, print_type: str) -> None:
        self.print_type = print_type

    def print_book(self, book: Book) -> None:
        if self.print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class SerializerJson(BookSerializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        if self.serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(BookSerializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        if self.serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")


# class SerializerHandler(SerializerJson, SerializerXML)
def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_processors = {
        "console": DisplayConsoleProcessor("console"),
        "reverse": DisplayReverseProcessor("reverse"),
    }

    printer_processors = {
        "console": PrinterConsoleProcessor("console"),
        "reverse": PrinterReverseProcessor("reverse"),
    }

    serializer_processors = {
        "json": SerializerJson("json"),
        "xml": SerializerXML("xml"),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_processor = display_processors.get(method_type)
            if display_processor:
                display_processor.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            printer_processor = printer_processors.get(method_type)
            if printer_processor:
                printer_processor.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serializer_processor = serializer_processors.get(method_type)
            if serializer_processor:
                return serializer_processor.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
