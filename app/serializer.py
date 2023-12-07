import json
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod

from . import BookABC


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: BookABC) -> str:
        pass


class SerializeToJSON(Serializer):
    @staticmethod
    def serialize(book: BookABC) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeToXML(Serializer):
    @staticmethod
    def serialize(book: BookABC) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")
