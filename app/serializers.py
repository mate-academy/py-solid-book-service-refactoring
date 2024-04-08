import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from app.book import Book


class SerializerBook(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class SerializerBookJSON(SerializerBook):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerBookXML(SerializerBook):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")
