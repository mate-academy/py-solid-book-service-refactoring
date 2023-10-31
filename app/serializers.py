from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET  # noqa


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(SerializerStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(SerializerStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = title
        content_element = ET.SubElement(root, "content")
        content_element.text = content
        return ET.tostring(root, encoding="unicode")
