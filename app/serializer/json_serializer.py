import json
from app.serializer.base import SerializerStrategy
from app.models import Book


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
