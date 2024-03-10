from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self, content: str) -> str:
        return content


class ReverseDisplay(Display):

    def display(self, content: str) -> str:
        return content[::-1]
