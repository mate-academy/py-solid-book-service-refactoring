from __future__ import annotations

import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElTr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class BookJSONSerializer(BookSerializer):
    def __init__(self, book: "Book") -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class BookXMLSerializer(BookSerializer):
    def __init__(self, book: "Book") -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = self.title
        content = ElTr.SubElement(root, "content")
        content.text = self.content
        return ElTr.tostring(root, encoding="unicode")


class BookSerializer:
    @staticmethod
    def serializer(book: "Book", type_serializer: str) -> None | str:
        if type_serializer == "json":
            return BookJSONSerializer(book).serialize()
        elif type_serializer == "xml":
            return BookXMLSerializer(book).serialize()
