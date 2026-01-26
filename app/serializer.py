import json
import xml.etree.ElementTree as ElemTree

from app.book import Book


class Serializer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def json_serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content})

    def xml_serialize(self) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElemTree.SubElement(root, "content")
        content.text = self.book.content
        return ElemTree.tostring(root, encoding="unicode")

    def serialize(self, method_type: str) -> str:
        method_name = f"{method_type}_serialize"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown serialize method: {method_type}")

        return method()
