import json
import xml.etree.ElementTree as ET  # noqa: N817
from app.interfaces import SerializeStrategy


class JSONSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        ET.SubElement(root, "title").text = title
        ET.SubElement(root, "content").text = content
        return ET.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def get_serializer(serialize_type: str) -> SerializeStrategy:
        if serialize_type == "json":
            return JSONSerializer()
        elif serialize_type == "xml":
            return XMLSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
