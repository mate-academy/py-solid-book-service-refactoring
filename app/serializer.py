import json
import xml.etree.ElementTree as ElementCase

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementCase.Element("book")
        title = ElementCase.SubElement(root, "title")
        title.text = book.title
        content = ElementCase.SubElement(root, "content")
        content.text = book.content
        return ElementCase.tostring(root, encoding="unicode")
