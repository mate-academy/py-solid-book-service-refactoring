from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class DisplayConsole(Display):
    def display(self, content: str) -> None:
        print(content)


class DisplayReverse(Display):
    def display(self, content: str) -> None:
        print(content[::-1])
