import json

from xml.etree.ElementTree import (
    Element,
    SubElement,
    tostring,
)


class Serializer:
    def serialize(self, title: str, content: str) -> str:
        raise NotImplementedError


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = Element("book")
        title_el = SubElement(root, "title")
        title_el.text = title
        content_el = SubElement(root, "content")
        content_el.text = content
        return tostring(root, encoding="unicode")


def get_serializer(serialize_type: str) -> Serializer:
    if serialize_type == "json":
        return JsonSerializer()
    if serialize_type == "xml":
        return XmlSerializer()
    raise ValueError(f"Unknown serialize type: {serialize_type}")
