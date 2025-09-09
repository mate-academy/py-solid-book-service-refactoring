import json
from serializer.base import Serializer
from models.book import Book


class SerializeJSON(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
