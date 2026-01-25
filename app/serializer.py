from __future__ import annotations

import json
import xml.etree.ElementTree as ElementTree
from typing import Dict, Protocol


class BookProtocol(Protocol):
    title: str
    content: str


class SerializerStrategy(Protocol):
    def serialize(self, book: BookProtocol) -> str:
        ...


class JsonSerializer:
    def serialize(self, book: BookProtocol) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )


class XmlSerializer:
    def serialize(self, book: BookProtocol) -> str:
        root = ElementTree.Element("book")

        title_element = ElementTree.SubElement(root, "title")
        title_element.text = book.title

        content_element = ElementTree.SubElement(root, "content")
        content_element.text = book.content

        return ElementTree.tostring(
            root,
            encoding="unicode",
        )


class BookSerializer:
    """Serializes a book using registered strategies."""

    def __init__(
        self,
        strategies: Dict[str, SerializerStrategy] | None = None,
    ) -> None:
        self._strategies: Dict[str, SerializerStrategy] = (
            strategies
            if strategies is not None
            else {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            }
        )

    def serialize(self, book: BookProtocol, serialize_type: str) -> str:
        if serialize_type not in self._strategies:
            raise ValueError(
                f"Unknown serialization type: {serialize_type}"
            )

        strategy = self._strategies[serialize_type]
        return strategy.serialize(book)
