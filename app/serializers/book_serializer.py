import json
from xml.etree.ElementTree import Element, SubElement, tostring

from app.book.book import Book


class BookSerializer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def json(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )

    def xml(self) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = self.book.title
        content = SubElement(root, "content")
        content.text = self.book.content
        return tostring(root, encoding="unicode")
