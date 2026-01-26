from __future__ import annotations

import json
import xml.etree.ElementTree as Element
import xml.etree.ElementTree as SubElement
import xml.etree.ElementTree as tostring  # noqa: N813

from abc import ABC, abstractmethod
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")


class SerializationService:
    _serializers: Dict[str, Serializer] = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    @classmethod
    def serialize(cls, book: Book, serialize_type: str) -> str:
        serializer = cls._serializers.get(serialize_type)
        if serializer is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serializer.serialize(book)
