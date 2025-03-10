import json

import xml.etree.ElementTree as Etree

from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = Etree.Element("book")
        title_elem = Etree.SubElement(root, "title")
        title_elem.text = book.title
        content_elem = Etree.SubElement(root, "content")
        content_elem.text = book.content
        return Etree.tostring(root, encoding="unicode")
