from abc import abstractmethod, ABC

from app.book import Book


class Print(ABC):
    @abstractmethod
    def print_console(self) -> None:
        pass

    @abstractmethod
    def print_reverse(self) -> None:
        pass

    @abstractmethod
    def print(self, method_type: str) -> None:
        pass


class PrintBook(Print):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_console(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print(self, method_type: str) -> None:
        if method_type == "reverse":
            self.print_reverse()
        elif method_type == "console":
            self.print_console()
