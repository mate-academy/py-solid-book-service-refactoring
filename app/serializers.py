import json
import xml.etree.ElementTree as EleT
from abc import ABC, abstractmethod

from app.books import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        ...


class SerializerToJson(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerToXml(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = EleT.Element("book")
        title = EleT.SubElement(root, "title")
        title.text = book.title
        content = EleT.SubElement(root, "content")
        content.text = book.content
        return EleT.tostring(root, encoding="unicode")
