import json
from app.models.book import Book
from xml.etree import ElementTree


class BookSerialize:
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps(
                {
                    "title": self.book.title,
                    "content": self.book.content
                }
            )
        elif serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.book.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.book.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
