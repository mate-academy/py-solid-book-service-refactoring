import json
import xml.etree.ElementTree as Etree

from abc import ABC, abstractmethod

from app.models import Book


class SerializationProcessor(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(SerializationProcessor):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializationProcessor):
    def serialize(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")
