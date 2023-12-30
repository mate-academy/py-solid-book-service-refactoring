import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class JsonSerializer(BaseSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BaseSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
