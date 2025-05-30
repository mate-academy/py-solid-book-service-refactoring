from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, data: dict) -> str:
        """Serialize the data into a string format."""
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str):
        root = ET.Element("book")
        title_elem = ET.SubElement(root, "title")
        title_elem.text = title
        content_elem = ET.SubElement(root, "content")
        content_elem.text = content
        return ET.tostring(root, encoding="unicode")
