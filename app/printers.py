from abc import ABC, abstractmethod


class Print(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintConsole(Print):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...", f"\n{self.content}")


class PrintReverse(Print):
    def print_book(self) -> None:
        print(
            f"Printing the book in reverse: {self.title}...",
            f"\n{self.content[::-1]}"
        )


class PrintFactory:
    """
    Factory to create the appropriate Display instance
    based on the display type.
    """

    @staticmethod
    def print_book(title: str, content: str, print_type: str) -> None:
        if print_type == "console":
            return PrintConsole(title=title, content=content).print_book()
        elif print_type == "reverse":
            return PrintReverse(title=title, content=content).print_book()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
