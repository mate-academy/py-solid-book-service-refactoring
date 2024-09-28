from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        """
        Should display the given content
        Returns: None

        """
        pass


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])
