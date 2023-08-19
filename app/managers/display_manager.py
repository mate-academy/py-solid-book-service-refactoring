from abc import ABC, abstractmethod


class DisplayManager(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class DisplayConsole(DisplayManager):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(DisplayManager):
    def display(self, content: str) -> None:
        print(content[::-1])
