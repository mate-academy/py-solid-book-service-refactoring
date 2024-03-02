import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book, ) -> str:
        pass


class JsonBookSerializer(BookSerializer):
    def serialize(self, book: Book, ) -> str:
        return json.dumps({"title": book.title,
                           "content": book.content},
                          )


class XmlBookSerializer(BookSerializer):
    def serialize(self, book: Book, ) -> str:
        root = ElementTree.Element("book.py")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
