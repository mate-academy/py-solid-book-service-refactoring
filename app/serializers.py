import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as Elem


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = Elem.Element("book")
        title_elem = Elem.SubElement(root, "title")
        title_elem.text = title
        content_elem = Elem.SubElement(root, "content")
        content_elem.text = content
        return Elem.tostring(root, encoding="unicode")
