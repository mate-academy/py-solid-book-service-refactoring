import json
import xml.etree.ElementTree as ElemTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializerBookProces(ABC):

    @abstractmethod
    def serialize_book(self) -> None:
        pass


class SerializeJson(SerializerBookProces):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize_book(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXml(SerializerBookProces):

    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize_book(self) -> str:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = self.title
        content = ElemTree.SubElement(root, "content")
        content.text = self.content
        return ElemTree.tostring(root, encoding="unicode")
