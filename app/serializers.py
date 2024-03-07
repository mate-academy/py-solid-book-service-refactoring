import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title, content):
        pass


class JsonSerializer(Serializer):
    def serialize(self, title, content):
        return json.dumps({"title": self, "content": self})


class XmlSerializer(Serializer):

    def serialize(self, title, content):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = title
        content = ET.SubElement(root, "content")
        content.text = content
        return ET.tostring(root, encoding="unicode")
