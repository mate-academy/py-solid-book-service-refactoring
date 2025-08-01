import json
import xml.etree.ElementTree as ElemTree
from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: "Book") -> ElemTree:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: "Book") -> ElemTree:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: "Book") -> ElemTree:
        root = ElemTree.Element("book")
        title = ElemTree.SubElement(root, "title")
        title.text = book.title
        content = ElemTree.SubElement(root, "content")
        content.text = book.content
        return ElemTree.tostring(root, encoding="unicode")
