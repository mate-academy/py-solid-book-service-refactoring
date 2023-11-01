import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class BaseSerializer(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self):
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerializer(BaseSerializer):
    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
