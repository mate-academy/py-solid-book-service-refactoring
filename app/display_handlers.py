from abc import ABC, abstractmethod

from app.books import Base


class DisplayHandler(Base, ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayHandler(DisplayHandler):

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayHandler(DisplayHandler):

    def display(self) -> None:
        print(self.book.content[::-1])
