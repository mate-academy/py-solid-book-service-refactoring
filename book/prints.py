from abc import abstractmethod, ABC

from book.book import Book


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookPrint:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            ConsolePrint().print_book(book)
        elif print_type == "reverse":
            ReversePrint().print_book(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
