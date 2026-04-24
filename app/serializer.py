from abc import ABC, abstractmethod
import json
from xml.etree import ElementTree

from app.models import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def get_serialize_type(serialize_type: str) -> BookSerializer:
    if serialize_type == "json":
        return JsonBookSerializer()
    elif serialize_type == "xml":
        return XmlBookSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
