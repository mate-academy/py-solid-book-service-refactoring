import json
import xml.etree.ElementTree as element_tree


def serialize_json(title: str, content: str) -> str:
    return json.dumps({"title": title, "content": content})


def serialize_xml(title: str, content: str) -> str:
    root = element_tree.Element("book")
    title_el = element_tree.SubElement(root, "title")
    title_el.text = title
    content_el = element_tree.SubElement(root, "content")
    content_el.text = content
    return ET.tostring(root, encoding="unicode")
