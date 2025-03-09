from abc import ABC, abstractmethod

from app.protocols import HasContent


class Displayer(ABC):
    @staticmethod
    @abstractmethod
    def display(obj: HasContent) -> str:
        pass


class ConsoleDisplayer(Displayer):
    @staticmethod
    def display(obj: HasContent) -> str:
        return obj.content


class ReverseDisplayer(Displayer):
    @staticmethod
    def display(obj: HasContent) -> str:
        return obj.content[::-1]
