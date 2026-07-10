import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

from app.book import Book


class SerializerType(ABC, Book):
    @abstractmethod
    def serialize(self):
        pass


class SerializerJSON(SerializerType):
    def serialize(self):
        return json.dumps({"title": self.title, "content": self.content})


class SerializerXML(SerializerType):
    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
