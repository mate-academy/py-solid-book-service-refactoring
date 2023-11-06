from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self) -> None:
        print(self.content)


class ReverseDisplay(DisplayStrategy):
    def display(self) -> None:
        print(self.content[::-1])
