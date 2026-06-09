import json
from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element, SubElement, tostring

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")


def get_serializer(serialize_type: str) -> Serializer:
    if serialize_type == "json":
        return JSONSerializer()
    elif serialize_type == "xml":
        return XMLSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
