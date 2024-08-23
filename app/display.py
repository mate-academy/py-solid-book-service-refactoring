from abc import ABC, abstractmethod


class DisplayType(ABC):

    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayType):

    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayType):

    def display(self, content: str) -> None:
        print(content[::-1])
