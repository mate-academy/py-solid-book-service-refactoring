
from app.display import DISPLAY_STRATEGIES
from app.printing import PRINT_STRATEGIES
from app.serialization import SERIALIZE_STRATEGIES


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
            raise ValueError(
                f"Unknown serialize type: {serialize_type}"
            )

        return strategy.serialize(self.title, self.content)
