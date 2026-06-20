import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(BaseSerializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content
        return ElementTree.tostring(root, encoding="unicode")


SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer()
}
