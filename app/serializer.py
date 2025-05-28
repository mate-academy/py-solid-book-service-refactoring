from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass

class JsonSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

class XmlSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_el = ET.SubElement(root, "title")
        title_el.text = title
        content_el = ET.SubElement(root, "content")
        content_el.text = content
        return ET.tostring(root, encoding="unicode")
