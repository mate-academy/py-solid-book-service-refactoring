from app.display_strategies import ConsoleDisplay, ReverseDisplay
from app.print_strategies import ConsolePrint, ReversePrint
from app.serialize_strategies import JsonSerializer, XmlSerializer

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        strategy = DISPLAY_STRATEGIES.get(display_type)
        if strategy is None:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self.content)

    def print_book(self, print_type: str) -> None:
        strategy = PRINT_STRATEGIES.get(print_type)
        if strategy is None:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        strategy = SERIALIZE_STRATEGIES.get(serialize_type)
        if strategy is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self.title, self.content)
