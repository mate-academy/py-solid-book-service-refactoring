import json
import xml.etree.ElementTree as ET # noqa
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self: Book) -> str:
        pass


class BooksSerializerJson(BookSerializer):

    def serialize(self: Book) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class BooksSerializerXML(BooksSerializerJson):

    def serialize(self: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
