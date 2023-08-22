import json

from xml.etree import ElementTree
from app.book import Book


class Serializer:
    @staticmethod
    def json_serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def xml_serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")

    @classmethod
    def serializer_by_type(cls, serialize_type: str, book: Book) -> str:
        if serialize_type == "json":
            return cls.json_serialize(book)
        elif serialize_type == "xml":
            return cls.xml_serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
