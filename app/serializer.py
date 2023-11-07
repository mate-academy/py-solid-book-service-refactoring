import json
import xml.etree.ElementTree as ElementCase

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlSerializer(Serializer):
    def serialize(self) -> str:
        root = ElementCase.Element("book")
        title = ElementCase.SubElement(root, "title")
        title.text = self.book.title
        content = ElementCase.SubElement(root, "content")
        content.text = self.book.content
        return ElementCase.tostring(root, encoding="unicode")
