import json
import xml.etree.ElementTree as ET

from app.models import Book


def json_serialize(book: Book) -> str:
    return json.dumps({"title": book.title, "content": book.content})

def xml_serialize(book: Book) -> str:
    root = ET.Element("book")
    title = ET.SubElement(root, "title")
    title.text = book.title
    content = ET.SubElement(root, "content")
    content.text = book.content
    return ET.tostring(root, encoding="unicode")

SERIALIZERS = {"json": json_serialize, "xml": xml_serialize}

def serialize(book: Book, serialize_type: str) -> str:
    if serialize_type in SERIALIZERS:
        return SERIALIZERS[serialize_type](book)
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
