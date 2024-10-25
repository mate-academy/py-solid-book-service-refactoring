import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree

from app.managers import Book


class SerializerBasic(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializerJSON(SerializerBasic):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(SerializerBasic):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
