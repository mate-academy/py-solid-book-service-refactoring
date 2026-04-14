from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, book) -> None:
        pass


class Console(Display):
    def display(self, book) -> None:
        print(book.content)


class Reverse(Display):
    def display(self, book) -> None:
        print(book.content[::-1])


class DisplayFactory(ABC):
    @staticmethod
    def get_display(display_type: str):
        if display_type == "console":
            return Console()
        elif display_type == "reverse":
            return Reverse()
        else:
            raise ValueError(f"Unknown display type: {display_type}")
