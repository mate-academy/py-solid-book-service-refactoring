import json
from typing import Dict, Callable
from xml.etree.ElementTree import ElementTree


class SerializeMixin:
    def __init__(self) -> None:
        self._serialize_methods: Dict[str, Callable[[], str]] = {
            "json": self._serialize_json,
            "xml": self._serialize_xml
        }

    def _serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def _serialize_xml(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")

    def serialize(self, serialize_type: str) -> str:
        method = self._serialize_methods.get(serialize_type)
        if method:
            return method()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
