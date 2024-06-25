import xml.etree.ElementTree as ElementTree
from app.serializers.serializer_strategy import SerializeStrategy


class XMLSerializeStrategy(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_elem = ElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = ElementTree.SubElement(root, "content")
        content_elem.text = content
        return ElementTree.tostring(root, encoding="unicode")
