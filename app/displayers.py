from abc import ABC, abstractmethod


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayer(BookDisplayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplayer(BookDisplayer):
    def display(self, content: str) -> None:
        print(content[::-1])
