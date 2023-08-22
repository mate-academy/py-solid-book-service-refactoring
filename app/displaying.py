from abc import ABC


class BookDisplay(ABC):
    def display(self, content: str) -> None:
        raise ValueError("Unknown display type.")


class BookDisplayConsole(BookDisplay):
    def display(self, content: str) -> None:
        print(content)


class BookDisplayReverse(BookDisplay):
    def display(self, content: str) -> None:
        print(content[::-1])
