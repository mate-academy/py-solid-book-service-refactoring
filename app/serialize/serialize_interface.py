import json
import xml.etree.ElementTree as eTree
from abc import ABC, abstractmethod

from app.book.book_model import Book


class SerializeInterface(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeInterface):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeInterface):
    def serialize(self, book: Book) -> str:
        root = eTree.Element("book")
        title = eTree.SubElement(root, "title")
        title.text = book.title
        content = eTree.SubElement(root, "content")
        content.text = book.content
        return eTree.tostring(root, encoding="unicode")
