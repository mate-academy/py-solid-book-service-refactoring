import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_elem = ET.SubElement(root, "title")
        title_elem.text = title
        content_elem = ET.SubElement(root, "content")
        content_elem.text = content
        return ET.tostring(root, encoding="unicode")
