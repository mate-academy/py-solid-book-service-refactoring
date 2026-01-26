from __future__ import annotations
from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as Element_tree

from .book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Element_tree.Element("book")

        title = Element_tree.SubElement(root, "title")
        title.text = book.title

        content = Element_tree.SubElement(root, "content")
        content.text = book.content

        return Element_tree.tostring(root, encoding="unicode")


def get_serializer(serialize_type: str) -> Serializer:
    if serialize_type == "json":
        return JsonSerializer()
    if serialize_type == "xml":
        return XmlSerializer()
    raise ValueError(f"Unknown serialize type: {serialize_type}")
