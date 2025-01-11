import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET # noqa

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonBookSerializer(Serializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(Serializer):
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def choose_serializer(serialize_type: str) -> Serializer:
    if serialize_type == "json":
        return JsonBookSerializer(serialize_type)
    elif serialize_type == "xml":
        return XMLBookSerializer(serialize_type)
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
