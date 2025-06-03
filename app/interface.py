from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
from .model import Book


class BookDisplayInterface(ABC):

    @abstractmethod
    def display(self, book: Book, method_type: str) -> None:
        pass


class BookPrintInterface(ABC):

    @abstractmethod
    def print_book(self, book: Book, method_type: str) -> None:
        pass


class BookSerializeInterface(ABC):

    @abstractmethod
    def serialize(self, book: Book, method_type: str) -> str:
        pass


class BookDisplay(BookDisplayInterface):

    def display(self, book: Book, display_type: str) -> None:
        if display_type == "console":
            print(book.content)
        elif display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrint(BookPrintInterface):

    def print_book(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookSerialize(BookSerializeInterface):

    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = book.title
            content = ET.SubElement(root, "content")
            content.text = book.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
