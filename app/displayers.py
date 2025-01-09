from abc import ABC, abstractmethod


class Display(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(Display):
    def display(self) -> None:
        print(self.content)


class DisplayReverse(Display):
    def display(self) -> None:
        print(self.content[::-1])


class DisplayFactory:
    """
    Factory to create the appropriate Display instance
    based on the display type.
    """

    @staticmethod
    def display(content: str, display_type: str) -> None:
        if display_type == "console":
            return DisplayConsole(content=content).display()
        elif display_type == "reverse":
            return DisplayReverse(content=content).display()
        raise ValueError(f"Unknown display type: {display_type}")
