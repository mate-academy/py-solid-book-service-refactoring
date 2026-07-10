import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as Element_tree

from app.book import Book


class SerializerType(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class SerializerJSON(SerializerType):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(SerializerType):
    def serialize(self, book: Book) -> str:
        root = Element_tree.Element("book")
        title = Element_tree.SubElement(root, "title")
        title.text = book.title
        content = Element_tree.SubElement(root, "content")
        content.text = book.content
        return Element_tree.tostring(root, encoding="unicode")
