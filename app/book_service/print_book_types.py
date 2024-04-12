from abc import ABC, abstractmethod


class PrintProcessor(ABC):

    @staticmethod
    @abstractmethod
    def print_book(title: str, content: str) -> None:
        pass


class ConsolePrintProcessor(PrintProcessor):

    @staticmethod
    def print_book(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintProcessor(PrintProcessor):

    @staticmethod
    def print_book(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
