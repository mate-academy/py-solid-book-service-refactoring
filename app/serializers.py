import json
import xml.etree.ElementTree as et
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        ...


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = et.Element("book")
        title = et.SubElement(root, "title")
        title.text = book.title
        content = et.SubElement(root, "content")
        content.text = book.content
        return et.tostring(root, encoding="unicode")
