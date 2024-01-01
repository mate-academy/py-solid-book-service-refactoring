from __future__ import annotations

import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book_model import Book


class BaseSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(instance: type) -> str:
        pass


class BaseJSONSerializer(BaseSerializer):
    @staticmethod
    @abstractmethod
    def serialize(instance: type) -> str:
        pass


class BaseXMLSerializer(BaseSerializer):
    @staticmethod
    @abstractmethod
    def serialize(instance: type) -> str:
        pass


# noinspection PyRedeclaration
class BookJSONSerializer(BaseJSONSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


# noinspection PyRedeclaration
class BookXMLSerializer(BaseXMLSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
