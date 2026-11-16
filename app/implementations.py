import json
import xml.etree.ElementTree as ET
from app.interfaces import (
    BookDisplayInterface,
    DetailBookInterface,
    SerializeBookInterface
)
from app.models import Book


class DisplayBookConsole(BookDisplayInterface):
    def display(self, book: Book) -> str:
        print(book.content)


class DisplayBookReverse(BookDisplayInterface):
    def display(self, book: Book) -> str:
        print(book.content[::-1])


class DetailTypeBook(DetailBookInterface):
    def print_book(self, book: Book) -> str:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class DetailTypeBookReverse(DetailBookInterface):
    def print_book(self, book: Book) -> str:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeBookJSON(SerializeBookInterface):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXML(SerializeBookInterface):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


displays = {
    "console": DisplayBookConsole,
    "reverse": DisplayBookReverse
}


printers = {
    "console": DetailTypeBook,
    "reverse": DetailTypeBookReverse
}


serializers = {
    "json": SerializeBookJSON,
    "xml": SerializeBookXML
}
