import json
import xml.etree.ElementTree as ElTree
from abc import ABC, abstractmethod

from app.errors import UnknownSerializerTypeError


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElTree.Element("book")
        title_el = ElTree.SubElement(root, "title")
        title_el.text = title
        content_el = ElTree.SubElement(root, "content")
        content_el.text = content
        return ElTree.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def create_serializer(method_type: str) -> Serializer:
        if method_type == "json":
            return JsonSerializer()
        elif method_type == "xml":
            return XmlSerializer()
        else:
            raise UnknownSerializerTypeError(
                "serializer", method_type
            )
