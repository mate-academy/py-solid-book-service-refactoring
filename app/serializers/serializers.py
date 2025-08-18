import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class SerializerInterface(ABC):
    @staticmethod
    @abstractmethod
    def serialize(title: str, content: str) -> str:
        pass


class JSONSerializer(SerializerInterface):
    @staticmethod
    def serialize(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(SerializerInterface):
    @staticmethod
    def serialize(title: str, content: str) -> str:
        root = ET.Element("book")
        sub_title = ET.SubElement(root, "title")
        sub_title.text = title
        sub_content = ET.SubElement(root, "content")
        sub_content.text = content
        return ET.tostring(root, encoding="unicode")
