import json
import xml.etree.ElementTree as ElementTree
from app.book import Book


class SerializerBook:
    def __init__(self, book: Book, serialize_type: str) -> None:
        self.book = book
        self.serialize_type = serialize_type

    def serialize(self) -> str:
        if self.serialize_type == "json":
            return json.dumps(
                {"title": self.book.title, "content": self.book.content}
            )
        elif self.serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.book.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.book.content
            return ElementTree.tostring(root, encoding="unicode")
