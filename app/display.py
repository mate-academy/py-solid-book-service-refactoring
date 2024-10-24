from abc import ABC, abstractmethod

from app.errors import UnknownDisplayTypeError


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayFactory:
    @staticmethod
    def create_display(method_type: str) -> Display:
        if method_type == "console":
            return ConsoleDisplay()
        elif method_type == "reverse":
            return ReverseDisplay()
        else:
            raise UnknownDisplayTypeError("display", method_type)
