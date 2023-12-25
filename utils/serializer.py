import json
import xml.etree.ElementTree as ET

from utils.base import Base


class Serializer(Base):
    def serialize_json(self):
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self, serialize_type: str) -> str:
        try:
             return getattr(self, f"serialize_{serialize_type}")()
        except AttributeError:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
