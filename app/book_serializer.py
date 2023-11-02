import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {"title": book.get_title(), "content": book.get_content()}
        )


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.get_title()
        content = ElementTree.SubElement(root, "content")
        content.text = book.get_content()
        return ElementTree.tostring(root, encoding="unicode")
