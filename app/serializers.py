import json
import xml.etree.ElementTree as eT
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):

    @staticmethod
    @abstractmethod
    def serialize_book(book: Book) -> None:
        pass


class JsonSerializer(Serializer):

    @staticmethod
    def serialize_book(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):

    @staticmethod
    def serialize_book(book: Book) -> str:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = book.title
        content = eT.SubElement(root, "content")
        content.text = book.content
        return eT.tostring(root, encoding="unicode")
