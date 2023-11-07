import json
from abc import ABC
from xml.etree import ElementTree

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self: Book) -> None:
        pass


class JsonSerializer(Serializer):
    def serialize(self: Book) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerializer(Serializer):
    def serialize(self: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
