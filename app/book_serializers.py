from abc import ABC, abstractmethod

import json
import xml.etree.ElementTree as ET  # noqa

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self) -> str:
        ...


class JsonSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XmlSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
