import json
import xml.etree.ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XmlBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")

        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title

        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content

        return xml.etree.ElementTree.tostring(
            root,
            encoding="unicode",
        )
