import json
import xml.etree.ElementTree as eT

from app.book import Book


class BookSerialization:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = eT.Element("book")
            title = eT.SubElement(root, "title")
            title.text = book.title
            content = eT.SubElement(root, "content")
            content.text = book.content
            return eT.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
