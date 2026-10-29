
from abc import ABC, abstractmethod


class BookDisplay(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(BookDisplay):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(BookDisplay):
    def display(self, content: str) -> None:
        print(content[::-1])


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}
