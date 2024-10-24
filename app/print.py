from abc import ABC, abstractmethod

from app.errors import UnknownPrintTypeError


class Print(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class PrintFactory:
    @staticmethod
    def create_print(method_type: str) -> Print:
        if method_type == "console":
            return ConsolePrint()
        elif method_type == "reverse":
            return ReversePrint()
        else:
            raise UnknownPrintTypeError("print", method_type)
