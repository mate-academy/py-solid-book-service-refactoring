from app.display import DisplayStrategy
from app.print import PrintStrategy
from app.serialize import SerializeStrategy


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_strategy: DisplayStrategy) -> None:
        display_strategy.display(self.content)

    def print(self, print_strategy: PrintStrategy) -> None:
        print_strategy.print(self.title, self.content)

    def serialize(self, serialize_strategy: SerializeStrategy) -> str:
        return serialize_strategy.serialize(self.title, self.content)
