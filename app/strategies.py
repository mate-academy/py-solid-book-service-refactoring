import json
import xml.etree.ElementTree as element_tree
from app.book import Book
from app.interfaces import (
    IDisplayStrategy,
    IPrintStrategy,
    ISerializerStrategy,
    IWriter
)


class GenericDisplayStrategy(IDisplayStrategy):
    def __init__(self, writer: IWriter) -> None:
        self.writer = writer


class ConsoleDisplay(GenericDisplayStrategy):
    def display(self, book: Book) -> None:
        self.writer.write(book.content)


class ReverseDisplay(GenericDisplayStrategy):
    def display(self, book: Book) -> None:
        self.writer.write(book.content[::-1])


class ConsolePrinter(IPrintStrategy):
    def __init__(self, writer: IWriter) -> None:
        self.writer = writer

    def print_book(self, book: Book) -> None:
        self.writer.write(f"Printing the book: {book.title}...")
        self.writer.write(book.content)


class ReversePrinter(IPrintStrategy):
    def __init__(self, writer: IWriter) -> None:
        self.writer = writer

    def print_book(self, book: Book) -> None:
        self.writer.write(f"Printing the book in reverse: {book.title}...")
        self.writer.write(book.content[::-1])


class JsonSerializer(ISerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(ISerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = element_tree.Element("book")
        title = element_tree.SubElement(root, "title")
        title.text = book.title
        content = element_tree.SubElement(root, "content")
        content.text = book.content
        return element_tree.tostring(root, encoding="unicode")
