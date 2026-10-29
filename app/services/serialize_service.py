import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from app.models.book import Book


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class SerializeService:
    def __init__(self, strategy: SerializeStrategy) -> None:
        self.strategy = strategy

    def serialize(self, book: Book) -> str:
        return self.strategy.serialize(book)


class SerializeStrategyFactory:
    @staticmethod
    def create(strategy_type: str) -> SerializeStrategy:
        strategies = {
            "json": JsonSerializeStrategy,
            "xml": XmlSerializeStrategy,
        }
        strategy_class = strategies.get(strategy_type)
        if strategy_class is None:
            raise ValueError(f"Unknown serialize type: {strategy_type}")
        return strategy_class()
