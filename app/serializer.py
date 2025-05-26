import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class IBookSerializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONBookSerializer(IBookSerializer):
    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content,
            }
        )


class XMLBookSerializer(IBookSerializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")


def select_serializer(method_type: str) -> type[IBookSerializer]:
    serializers = {
        "json": JSONBookSerializer,
        "xml": XMLBookSerializer,
    }

    return serializers[method_type]
