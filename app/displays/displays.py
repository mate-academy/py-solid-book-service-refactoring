from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    @staticmethod
    @abstractmethod
    def display(content: str) -> None:
        pass


class DisplayConsole(DisplayInterface):
    @staticmethod
    def display(content: str) -> None:
        print(content)


class DisplayReverse(DisplayInterface):
    @staticmethod
    def display(content: str) -> None:
        print(content[::-1])
