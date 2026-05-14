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
    display_types = {
        "console": DisplayConsoleBook,
        "reverse": DisplayReverseBook,
    }
    if display_type in display_types:
        display_class = display_types.get(display_type)
        display_class(content=content).display()
    else:
        raise ValueError(f"Unknown display type: {display_type}")
