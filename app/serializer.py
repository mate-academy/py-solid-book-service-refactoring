import json
import xml.etree.ElementTree as ET


class Serializer:
    def serialize(self, data: dict) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        return json.dumps(data)


class XmlSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        root = ET.Element("book")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = value
        return ET.tostring(root, encoding="unicode")
