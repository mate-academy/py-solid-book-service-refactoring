from app.interfaces import IPrintStrategy, IDisplayStrategy
from app.display_strategies import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy,
)


class ConsolePrintStrategy(IPrintStrategy):
    def __init__(self, display_strategy: IDisplayStrategy = None) -> None:
        self.display_strategy = \
            display_strategy if display_strategy else ConsoleDisplayStrategy()

    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        self.display_strategy.display(content)


class ReversePrintStrategy(IPrintStrategy):
    def __init__(self, display_strategy: IDisplayStrategy = None) -> None:
        self.display_strategy = \
            display_strategy if display_strategy else ReverseDisplayStrategy()

    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        self.display_strategy.display(content)
