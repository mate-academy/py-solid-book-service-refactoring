import json
from xml.etree import ElementTree as eT
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize_book(book: Book) -> None:
        pass


class JSONSerializer(Serializer):
    @staticmethod
    def serialize_book(book: Book) -> json:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    @staticmethod
    def serialize_book(book: Book) -> eT:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = book.title
        content = eT.SubElement(root, "content")
        content.text = book.content
        return eT.tostring(root, encoding="unicode")
