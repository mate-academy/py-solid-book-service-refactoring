from app.display import DisplayStrategy
from app.serializer import SerializationStrategy
from app.print import PrintStrategy


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.content)

    def serialize(self, strategy: SerializationStrategy) -> str:
        return strategy.serialize(self.title, self.content)

    def print(self, strategy: PrintStrategy) -> None:
        strategy.print(self.title, self.content)
