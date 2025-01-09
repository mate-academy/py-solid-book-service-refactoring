from app.displayers import DisplayFactory
from app.printers import PrintFactory
from app.serializers import SerializerFactory


class Book:
    def __init__(self, *args) -> None:
        self.title, self.content = args

    def serialize(self, serialize_type: str) -> str:
        return SerializerFactory.serialize(
            self.title, self.content, serialize_type
        )

    def display(self, display_type: str) -> None:
        DisplayFactory.display(
            self.content, display_type
        )

    def print_book(self, print_type: str) -> None:
        PrintFactory.print_book(
            self.title, self.content, print_type
        )
