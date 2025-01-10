import json
import xml.etree.ElementTree
from app.book import Book


class SerializeBook:
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps(
                {"title": self.book.title, "content": self.book.content}
            )
        elif serialize_type == "xml":
            root = xml.etree.ElementTree.Element("book")
            title = xml.etree.ElementTree.SubElement(root, "title")
            title.text = self.book.title
            content = xml.etree.ElementTree.SubElement(root, "content")
            content.text = self.book.content
            return xml.etree.ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
