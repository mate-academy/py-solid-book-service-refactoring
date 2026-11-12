import json
from abc import ABC
from xml.etree import ElementTree

from app.models import Book


class BookOutputOperation(ABC):
    def output(self, book: Book) -> None | str:
        pass


class ConsoleDisplay(BookOutputOperation):
    def output(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookOutputOperation):
    def output(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolPrint(BookOutputOperation):
    def output(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BookOutputOperation):
    def output(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class JsonSerializer(BookOutputOperation):
    def output(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookOutputOperation):
    def output(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
