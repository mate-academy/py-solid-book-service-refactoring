import json
import xml.etree.ElementTree as ET


def serialize_book(title: str, content: str, serialize_type: str) -> str:
    if serialize_type == "json":
        return json.dumps({"title": title, "content": content})
    elif serialize_type == "xml":
        root = ET.Element("book")
        title_el = ET.SubElement(root, "title")
        title_el.text = title
        content_el = ET.SubElement(root, "content")
        content_el.text = content
        return ET.tostring(root, encoding="unicode")
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")