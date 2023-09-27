import json
import xml.etree.ElementTree as Et


class Serializer:
    def serialize(self, data: dict) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        return json.dumps(data)


class XmlSerializer(Serializer):
    def serialize(self, data: dict) -> str:
        root = Et.Element("book")
        for key, value in data.items():
            element = Et.SubElement(root, key)
            element.text = value
        return Et.tostring(root, encoding="unicode")
