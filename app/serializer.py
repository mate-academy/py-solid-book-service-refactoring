import json
from abc import ABC, abstractmethod

import xml.etree.ElementTree as ElemT

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElemT.Element("book")
        title = ElemT.SubElement(root, "title")
        title.text = book.title
        content = ElemT.SubElement(root, "content")
        content.text = book.content
        return ElemT.tostring(root, encoding="unicode")
