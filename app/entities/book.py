from app.services.display_service import display_content
from app.services.print_service import print_book_content
from app.serializers.serializer import serialize_book


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __str__(self):
        return ("Book name is: {self.title}")

    def display(self, display_type: str) -> None:
        display_content(self.content, display_type)

    def print_book(self, print_type: str) -> None:
        print_book_content(self.title, self.content, print_type)

    def serialize(self, serialize_type: str) -> str:
        return serialize_book(self.title, self.content, serialize_type)