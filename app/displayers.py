from abc import ABC, abstractmethod

from app.base import Base


class Displayer(ABC, Base):

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayer(Displayer):

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayer(Displayer):

    def display(self) -> None:
        print(self.book.content[::-1])
