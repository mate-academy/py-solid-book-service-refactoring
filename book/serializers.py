import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree

from book.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: "Book") -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: "Book") -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: "Book") -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
