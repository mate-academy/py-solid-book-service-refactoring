import json

from app.book import Book
from app.serializer.base import BaseSerializer


class JsonSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {
                "title": book.title,
                "content": book.content,
            }
        )
