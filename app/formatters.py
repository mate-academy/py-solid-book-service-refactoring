import json
import xml.etree.ElementTree as ET
from app.interfaces import BookAction
from app.models import Book


class ConsoleDisplay(BookAction):
    def execute(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookAction):
    def execute(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter(BookAction):
    def execute(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class ReversePrinter(BookAction):
    def execute(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content[::-1]}")


class BookJSONSerializer(BookAction):
    def execute(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookXMLSerializer(BookAction):
    def execute(self, book: Book) -> str:
        root = ET.Element("book")
        ET.SubElement(root, "title").text = book.title
        ET.SubElement(root, "content").text = book.content
        return ET.tostring(root, encoding="unicode")
