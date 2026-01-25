import json
import xml.etree.ElementTree as ElementTree


class BookSerializer:
    """Handles book serialization into different formats."""

    def serialize(self, book, serialize_type: str) -> str:
        if serialize_type == "json":
            return self._serialize_to_json(book)

        if serialize_type == "xml":
            return self._serialize_to_xml(book)

        raise ValueError(f"Unknown serialization type: {serialize_type}")

    def _serialize_to_json(self, book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )

    def _serialize_to_xml(self, book) -> str:
        root = ElementTree.Element("book")

        title_element = ElementTree.SubElement(root, "title")
        title_element.text = book.title

        content_element = ElementTree.SubElement(root, "content")
        content_element.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
