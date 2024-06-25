from abc import ABC, abstractmethod
import json
import dicttoxml

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        book_data = {"title": book.title, "content": book.content}
        return dicttoxml.dicttoxml(
            book_data,
            custom_root="book",
            attr_type=False).decode("utf-8")
