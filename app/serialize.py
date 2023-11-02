import abc

import json
from xml.etree import ElementTree

from app.book import Book


class Serializer(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def serialize(book: Book) -> str:
        ...


class SerializerJSON(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
