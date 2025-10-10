from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayPrintBook(ABC, Book):
    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsoleBook(DisplayPrintBook):
    def display(self) -> None:
        print(self.content)

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReverseBook(DisplayPrintBook):
    def display(self) -> None:
        print(self.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
