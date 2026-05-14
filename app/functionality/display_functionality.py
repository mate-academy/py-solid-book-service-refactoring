from abc import ABC, abstractmethod


class DisplayBook(ABC):
    def __init__(self, content: str) -> None:
        self.content = content

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsoleBook(DisplayBook):
    def display(self) -> None:
        print(self.content)


class DisplayReverseBook(DisplayBook):
    def display(self) -> None:
        print(self.content[::-1])


def display_book_func(display_type: str, content: str) -> None:
    if display_type == "console":
        DisplayConsoleBook(content).display()
    elif display_type == "reverse":
        DisplayReverseBook(content).display()
    else:
        raise ValueError(f"Unknown display type: {display_type}")
