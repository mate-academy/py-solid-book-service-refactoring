from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content) -> None:
        pass


class DisplayConsole(Display):
    def display(self, content) -> None:
        print(content)


class DisplayReverse(Display):
    def display(self, content) -> None:
        print(content[::-1])
