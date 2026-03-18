import json
from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element, SubElement, tostring

from app.models import Book


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = Element("book")

        title = SubElement(root, "title")
        title.text = book.title

        content = SubElement(root, "content")
        content.text = book.content

        return tostring(root, encoding="unicode")


def get_serializer(serialize_type: str) -> SerializeStrategy:
    if serialize_type == "json":
        return JsonSerializer()
    elif serialize_type == "xml":
        return XmlSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
