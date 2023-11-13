from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display_func(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display_func(self, content: str) -> None:
        print(content)


class ReverseConsoleDisplay(Display):
    def display_func(self, content: str) -> None:
        print(content[::-1])
