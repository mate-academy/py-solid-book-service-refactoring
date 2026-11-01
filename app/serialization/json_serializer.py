import json

from app.book import Book
from app.serialization.base import SerializeBook


class SerializeBookJson(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
