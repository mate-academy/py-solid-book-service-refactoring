import json
import xml.etree.ElementTree as Et
from app.interfaces import Serializer


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        title_elem = Et.SubElement(root, "title")
        title_elem.text = title
        content_elem = Et.SubElement(root, "content")
        content_elem.text = content
        return Et.tostring(root, encoding="unicode")


class SerializerFactory:
    _serializers = {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    }

    @staticmethod
    def create_serializer(serialize_type: str) -> Serializer:
        serializer_class = SerializerFactory._serializers.get(serialize_type)
        if serializer_class is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serializer_class()
