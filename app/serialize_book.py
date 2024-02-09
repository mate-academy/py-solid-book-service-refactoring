import json
import xml.etree.ElementTree as eTree
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class BookJsonSerialize(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookXMLSerialize(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = eTree.Element("book")
        title = eTree.SubElement(root, "title")
        title.text = book.title
        content = eTree.SubElement(root, "content")
        content.text = book.content
        return eTree.tostring(root, encoding="unicode")
