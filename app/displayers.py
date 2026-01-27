from abc import ABC, abstractmethod


class Displayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayer(Displayer):
    def display(self, content: str) -> None:
        print(content[::-1])
