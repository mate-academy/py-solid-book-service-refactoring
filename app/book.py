from app.display import Display
from app.printer import Print
from app.serializer import Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, method: Display) -> None:
        method.display(self.content)

    def serialize(self, method: Serializer) -> str:
        return method.serialize(self.title, self.content)

    def print(self, method: Print) -> None:
        method.print(self.title, self.content)
