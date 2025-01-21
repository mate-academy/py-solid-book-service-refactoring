from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, title: str, content: str) -> None:
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, title: str, content: str) -> None:
        print(content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, title: str, content: str) -> None:
        print(content[::-1])
