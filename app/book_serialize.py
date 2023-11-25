import json
import xml.etree.ElementTree as Et

from app.book import Book


class BookSerialize:
    def __init__(self, book: Book) -> None:
        self.book = book

    def json(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )

    def xml(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.book.title
        content = Et.SubElement(root, "content")
        content.text = self.book.content
        return Et.tostring(root, encoding="unicode")
