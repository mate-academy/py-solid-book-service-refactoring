import json

from xml.etree import ElementTree
from app.book import Book


class Serialize:
    @staticmethod
    def serialize_json(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def serialize_xlm(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")

    @classmethod
    def serialize(cls, book: Book, method_type: str) -> str:
        if method_type == "json":
            return cls.serialize_json(book)
        elif method_type == "xml":
            return cls.serialize_xlm(book)
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")
