from app.display import DisplayStrategy
from app.print import PrintStrategy
from app.serializer import SerializeStrategy


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.content)

    def print_book(self, strategy: PrintStrategy) -> None:
        strategy.print(self.title, self.content)

    def serialize(self, strategy: SerializeStrategy) -> str:
        return strategy.serialize(self.title, self.content)
