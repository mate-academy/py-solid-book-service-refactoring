from app.display import DisplayType
from app.print import PrintType
from app.serialize import SerializeType


class Book:

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: DisplayType) -> None:
        display_type.display(self.content)

    def print(self, print_type: PrintType) -> None:
        print_type.print(self.title, self.content)

    def serialize(self, serialize_type: SerializeType) -> str:
        return serialize_type.serialize(self.title, self.content)
