import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.books import Book


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


def get_serialize_strategy(serialize_type: str) -> SerializeStrategy:
    if serialize_type == "json":
        return JsonSerialize()
    elif serialize_type == "xml":
        return XmlSerialize()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
