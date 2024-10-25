import json
import xml.etree.ElementTree as ElementTree

from app.book import Book


class BookSerializer:
    def serialize(self, book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = book.title
            content = ElementTree.SubElement(root, "content")
            content.text = book.content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
