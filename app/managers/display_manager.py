from abc import ABC, abstractmethod


class DisplayManager(ABC):
    def __init__(self) -> None:
        self.content: str = None  # Type annotation for instance variable

    @abstractmethod
    def display(self, content: str) -> None:
        self.content = content


class DisplayConsole(DisplayManager):
    def __init__(self) -> None:
        super().__init__()

    def display(self, content: str) -> None:
        super().display(content)
        print(self.content)


class DisplayReverse(DisplayManager):
    def __init__(self) -> None:
        super().__init__()

    def display(self, content: str) -> None:
        super().display(content)
        print(self.content[::-1])
