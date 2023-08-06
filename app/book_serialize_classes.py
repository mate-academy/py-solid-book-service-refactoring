import json

from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree

from app.book import Book


class BookSerializer(ABC):

    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class BookSerializerJSON(BookSerializer):

    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookSerializerXML(BookSerializer):

    @staticmethod
    def serialize(book: Book) -> ElementTree:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
