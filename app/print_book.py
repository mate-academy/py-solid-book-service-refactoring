import abc


class PrintBook(abc.ABC):
    def __init__(self, content: str, title: str) -> None:
        self.content = content
        self.title = title

    @abc.abstractmethod
    def print_book(self) -> None:
        ...


class PrintConsole(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverse(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
