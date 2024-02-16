from app.display_methods import DisplayMethod
from app.print_methods import PrintMethod
from app.serialize_methods import SerializeMethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_strategy: DisplayMethod) -> None:
        display_strategy.display(self.content)

    def print_book(self, print_strategy: PrintMethod) -> None:
        print_strategy.print_book(self.title, self.content)

    def serialize(self, serialize_strategy: SerializeMethod) -> str:
        return serialize_strategy.serialize(self.title, self.content)
