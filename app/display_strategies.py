from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class DisplayConsole(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class Display:
    def __init__(self, strategy: DisplayStrategy) -> None:
        self.strategy = strategy

    def display(self, content: str) -> None:
        self.strategy.display(content)
