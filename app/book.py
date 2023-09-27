from app.display import Display
from app.serializer import Serializer
from app.print import Print


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def perform_display(self, display: Display) -> None:
        display.display(self.content)

    def perform_print(self, print_method: Print) -> None:
        print_method.print(self.title, self.content)

    def serialize(self, serializer: Serializer) -> str:
        data = {"title": self.title, "content": self.content}
        return serializer.serialize(data)
