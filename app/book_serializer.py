import json
import xml.etree.ElementTree as ET  # noqa
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self._book = book

    def serialize(self) -> str:
        return json.dumps(
            {"title": self._book.title, "content": self._book.content}
        )


class XmlSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self._book = book

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self._book.title
        content = ET.SubElement(root, "content")
        content.text = self._book.content

        return ET.tostring(root, encoding="unicode")
