import json
import xml.etree.ElementTree as ETree

from app.book import Book


class Serializer:
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
            root = ETree.Element("book")
            title = ETree.SubElement(root, "title")
            title.text = self.book.title
            content = ETree.SubElement(root, "content")
            content.text = self.book.content
            serialized_xml = ETree.tostring(root, encoding="unicode")
            return serialized_xml
        raise ValueError(f"Unknown serialize type: {serialize_type}")
