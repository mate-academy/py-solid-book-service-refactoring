import json
from xml.etree import ElementTree

from app.book import Book


class Serializer:
    @classmethod
    def serialize(cls, book: Book) -> None:
        raise ValueError("Unknown serialize type")


class JsonSerializer(Serializer):
    @classmethod
    def serialize(cls, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    @classmethod
    def serialize(cls, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
