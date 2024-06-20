import json
import xml.etree.ElementTree as Etree
from abc import ABC, abstractmethod


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = Etree.Element("book")
        title_element = Etree.SubElement(root, "title")
        title_element.text = title
        content_element = Etree.SubElement(root, "content")
        content_element.text = content
        return Etree.tostring(root, encoding="unicode")
