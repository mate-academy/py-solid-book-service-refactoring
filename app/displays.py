from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, display_type: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, display_type: str) -> None:
        print(display_type)


class ReverseDisplay(Display):
    def display(self, display_type: str) -> None:
        print(display_type[::-1])
