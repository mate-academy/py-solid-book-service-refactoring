import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializeBook(SerializeBook):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XMLSerializeBook(SerializeBook):
    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = title
        content = ET.SubElement(root, "content")
        content.text = content
        return ET.tostring(root, encoding="unicode")
