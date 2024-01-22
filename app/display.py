from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, book: object) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: object) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: object) -> None:
        print(book.content[::-1])
