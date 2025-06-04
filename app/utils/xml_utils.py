import xml.etree.ElementTree as elementTree


def to_xml(title: str, content: str) -> str:
    root = elementTree.Element("book")
    title_elem = elementTree.SubElement(root, "title")
    title_elem.text = title
    content_elem = elementTree.SubElement(root, "content")
    content_elem.text = content
    return elementTree.tostring(root, encoding="unicode")
