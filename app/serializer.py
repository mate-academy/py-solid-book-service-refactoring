import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as eT
from typing import Any


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(Serializer):
    def __init__(self, book: Any) -> None:
        self.book = book

    def serialize(self) -> Any:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLSerializer(Serializer):
    def __init__(self, book: Any) -> None:
        self.book = book

    def serialize(self) -> Any:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = self.book.title
        content = eT.SubElement(root, "content")
        content.text = self.book.content
        return eT.tostring(root, encoding="unicode")
