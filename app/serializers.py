import json
import xml.etree.ElementTree as ElementTree

from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class SerializerJson(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXml(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
