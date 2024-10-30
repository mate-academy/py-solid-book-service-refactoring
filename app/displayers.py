from abc import ABC, abstractmethod


class BaseDisplay(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(BaseDisplay):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(BaseDisplay):
    def display(self, content: str) -> None:
        print(content[::-1])
