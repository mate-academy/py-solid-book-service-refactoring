from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as eTree

from app.book import Book


class BookSerializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({
            "title": book.get_title(), "content": book.get_content()
        })


class XMLSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        root = eTree.Element("book")
        title = eTree.SubElement(root, "title")
        title.text = book.get_title()
        content = eTree.SubElement(root, "content")
        content.text = book.get_content()
        return eTree.tostring(root, encoding="unicode")
