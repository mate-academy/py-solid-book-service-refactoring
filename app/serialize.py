import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serialize(ABC):
    def __init__(self, book: Book) -> None:
        self._book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self) -> None:
        return json.dumps(
            {"title": self._book.title, "content": self._book.content}
        )


class SerializeXml(Serialize):
    def serialize(self) -> None:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self._book.title
        content = Et.SubElement(root, "content")
        content.text = self._book.content
        return Et.tostring(root, encoding="unicode")
