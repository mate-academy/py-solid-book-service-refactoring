import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> json:
        pass

    @staticmethod
    def get_serializer_class(given_type: str) -> "Serializer":
        if given_type == "xml":
            return XMLSerializer

        elif given_type == "json":
            return JSONSerializer

        else:
            raise ValueError(f"Unknown serialize type: {given_type}")


class XMLSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class JSONSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
