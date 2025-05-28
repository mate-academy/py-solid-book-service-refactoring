import json
from abc import ABC
import xml.etree.ElementTree as elementTree
from app.book import Book


class Serializer(ABC):
    def serialize(self, book: Book) -> str:
        pass


class SerializerJson(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(Serializer):
    def serialize(self, book: Book) -> str:
        root = elementTree.Element("book")
        title = elementTree.SubElement(root, "title")
        title.text = book.title
        content = elementTree.SubElement(root, "content")
        content.text = book.content
        return elementTree.tostring(root, encoding="unicode")
