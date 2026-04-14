from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_book(self, book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrinterFactory(ABC):
    @staticmethod
    def get_printer(print_type: str):
        if print_type == "console":
            return ConsolePrinter()
        elif print_type == "reverse":
            return ReversePrinter()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
