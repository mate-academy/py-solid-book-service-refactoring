from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET  # noqa


class SerializerStrategy(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(SerializerStrategy):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerializer(SerializerStrategy):
    def serialize(self) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = self.title
        content_element = ET.SubElement(root, "content")
        content_element.text = self.content
        return ET.tostring(root, encoding="unicode")
