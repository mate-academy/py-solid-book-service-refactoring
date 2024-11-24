from abc import ABC, abstractmethod


class DisplayMethod(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayMethod):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayMethod):
    def display(self, content: str) -> None:
        print(content[::-1])
