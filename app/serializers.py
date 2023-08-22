from abc import ABC, abstractmethod

import json
import xml.etree.ElementTree as ET

from app.book import Book


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class BookSerializerJSON(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookSerializerXML(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content

        return ET.tostring(root, encoding="unicode")
