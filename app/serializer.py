import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from . import BookABC


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: BookABC) -> str:
        pass


class SerializeToJSON(Serializer):
    def serialize(book: BookABC) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeToXML(Serializer):
    def serialize(book: BookABC) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
