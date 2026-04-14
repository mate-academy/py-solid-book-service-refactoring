from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, book) -> None:
        pass


class Console(Display):
    def display(self, book) -> None:
        print(book.content)


class Reverse(Display):
    def display(self, book) -> None:
        print(book.content[::-1])
