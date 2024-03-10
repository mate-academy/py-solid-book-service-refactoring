from __future__ import annotations
import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.main import Book


class BookSerializer(ABC):
    @abstractmethod
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XmlBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        super().__init__(book)

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.book.title
        content = Et.SubElement(root, "content")
        content.text = self.book.content
        return Et.tostring(root, encoding="unicode")
