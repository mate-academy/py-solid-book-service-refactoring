import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = book.title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
