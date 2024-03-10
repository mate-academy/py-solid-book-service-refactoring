import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> None:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> json:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):

    def serialize(self, title_text: str, content_text: str) -> ET:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = title_text
        content = ET.SubElement(root, "content")
        content.text = content_text
        return ET.tostring(root, encoding="unicode")
