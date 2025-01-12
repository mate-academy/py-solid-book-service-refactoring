from xml.etree import ElementTree

from app.interfaces import BookOperation


class XmlSerializer(BookOperation):
    """Serialize content to XML format."""

    def process(self, content: str, title: str | None = None) -> str:
        root = ElementTree.Element("book")

        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title

        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content

        return ElementTree.tostring(root, encoding="unicode")
