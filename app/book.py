from app.serializers import (
    DisplayInterface,
    PrintBookInterface,
    SerializeInterface
)


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_interface: DisplayInterface) -> None:
        display_interface.display(self.content)

    def print_book(self, print_interface: PrintBookInterface) -> None:
        print_interface.print_book(self.title, self.content)

    def serialize(self, serialize_interface: SerializeInterface) -> str:
        return serialize_interface.serialize(self.title, self.content)
