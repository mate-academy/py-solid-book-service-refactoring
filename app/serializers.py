import json
import xml.etree.ElementTree as Et
from abc import abstractmethod, ABC


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        title_element = Et.SubElement(root, "title")
        title_element.text = title
        content_element = Et.SubElement(root, "content")
        content_element.text = content
        return Et.tostring(root, encoding="unicode")
