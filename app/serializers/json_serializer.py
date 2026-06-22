import json
from app.models.book import Book
from app.serializers.base import Serializer


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
