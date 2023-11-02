import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Serializer(ABC):

    @staticmethod
    def serialize(book):
        pass


class JsonSerializer(Serializer):
    @staticmethod
    def serialize(book):
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    @staticmethod
    def serialize(book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
