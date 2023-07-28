import json
import xml.etree.ElementTree


class JsonSerialize:
    @staticmethod
    def serialize(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize:
    @staticmethod
    def serialize(title: str, content: str) -> str:
        root = xml.etree.ElementTree.Element("book")
        title_element = xml.etree.ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = xml.etree.ElementTree.SubElement(root, "content")
        content_element.text = content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
