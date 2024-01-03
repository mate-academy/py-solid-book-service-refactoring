from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElTr

from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class JSONSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title,
                           "content": book.content})


class XMLSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = book.title
        content = ElTr.SubElement(root, "content")
        content.text = book.content
        return ElTr.tostring(root, encoding="unicode")
