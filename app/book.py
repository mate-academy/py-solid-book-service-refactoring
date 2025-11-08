from app.display_strategies import DisplayStrategyFactory
from app.print_strategies import PrintStrategyFactory
from app.serializers import SerializerFactory


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        strategy = DisplayStrategyFactory.get_strategy(display_type)
        strategy.display(self)

    def print_book(self, print_type: str) -> None:
        strategy = PrintStrategyFactory.get_strategy(print_type)
        strategy.print_book(self)

    def serialize(self, serialize_type: str) -> str:
        serializer = SerializerFactory.get_serializer(serialize_type)
        return serializer.serialize(self)
