import json

from app.interfaces import BookOperation


class JsonSerializer(BookOperation):
    """Serialize content to JSON format."""

    def process(self, content: str, title: str | None = None) -> str:
        return json.dumps({"title": title, "content": content})
