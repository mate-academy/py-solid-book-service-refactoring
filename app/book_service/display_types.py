from abc import ABC, abstractmethod


class DisplayProcessor(ABC):

    @staticmethod
    @abstractmethod
    def display(content: str) -> None:
        pass


class ConsoleDisplayProcessor(DisplayProcessor):

    @staticmethod
    def display(content: str) -> None:
        print(content)


class ReverseDisplayProcessor(DisplayProcessor):

    @staticmethod
    def display(content: str) -> None:
        print(content[::-1])
