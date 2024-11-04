from abc import ABC, abstractmethod


class BasePrintBook(ABC):

    @abstractmethod
    def print_book(self, print_type: str) -> None:
        pass


class ConsolePrintBook(BasePrintBook):

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        else:
            super().print_book(print_type)


class ReversePrintBook(BasePrintBook):
    def print_book(self, print_type: str) -> None:
        if print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            super().print_book(print_type)


class PrintBook(ReversePrintBook, ConsolePrintBook):
    pass
