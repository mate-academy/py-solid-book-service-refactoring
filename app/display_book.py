from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, content: str) -> str:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> str:
        return content


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> str:
        return content[::-1]
