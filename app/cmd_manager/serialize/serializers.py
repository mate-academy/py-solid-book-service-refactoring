from abc import ABC, abstractclassmethod
from xml.etree import ElementTree
import json

from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractclassmethod
    def serialize(book: Book) -> None:
        pass


class JsonSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")

        title = ElementTree.SubElement(root, "title")
        title.text = book.title

        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
