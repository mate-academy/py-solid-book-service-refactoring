import json

from app.models.models import Book
from app.serializers.base import SerializerStrategy


class JsonSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
