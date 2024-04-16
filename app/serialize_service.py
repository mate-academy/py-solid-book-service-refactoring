import json
import xml.etree.ElementTree as ElementTree


class SerializeService:
    @staticmethod
    def serialize(title: str, content: str, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": title, "content": content})
        elif serialize_type == "xml":
            root = ElementTree.Element("book")
            title_elem = ElementTree.SubElement(root, "title")
            title_elem.text = title
            content_elem = ElementTree.SubElement(root, "content")
            content_elem.text = content
            return ElementTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
