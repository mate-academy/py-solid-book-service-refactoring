from abc import abstractmethod, ABC


class Printer(ABC):
    @abstractmethod
    def print_book(self, book_title: str, book_content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book_title: str, book_content: str) -> None:
        print(f"Printing the book: {book_title}...")
        print(book_content)


class ReversePrinter(Printer):
    def print_book(self, book_title: str, book_content: str) -> None:
        print(f"Printing the book in reverse: {book_title}...")
        print(book_content[::-1])
