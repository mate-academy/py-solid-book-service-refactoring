from abc import ABC, abstractmethod


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleBookDisplayer(BookDisplayer):
    def display(self, content: str) -> None:
        print(content)


class ReverseBookDisplayer(BookDisplayer):
    def display(self, content: str) -> None:
        print(content[::-1])
