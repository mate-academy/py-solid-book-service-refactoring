import json
from abc import ABC, abstractmethod
from typing import Mapping, TypeVar
from xml.etree import ElementTree

from app.Models import Book

T = TypeVar("T")


def get_strategy(registry: Mapping[str, T], key: str, kind: str) -> T:
    try:
        return registry[key]
    except KeyError:
        raise ValueError(f"Unknown {kind} type: {key}") from None


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")
