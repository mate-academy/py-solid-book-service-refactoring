from abc import ABC, abstractmethod


class DisplayType(ABC):

    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayType(DisplayType):

    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayType(DisplayType):
    def display(self, content: str) -> None:
        print(content[::-1])
