from abc import ABC, abstractmethod


class PrintBook(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintConsoleBook(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverseBook(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


def print_book_func(print_type: str, title: str, content: str) -> None:
    if print_type == "console":
        PrintConsoleBook(title, content).print_book()
    elif print_type == "reverse":
        PrintReverseBook(title, content).print_book()
    else:
        raise ValueError(f"Unknown print type: {print_type}")
