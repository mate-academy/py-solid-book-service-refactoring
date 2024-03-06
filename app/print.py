from abc import ABC, abstractmethod
from app.book import Book


class PrintCMD(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsolePrint(PrintCMD):
    def display(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintCMD):
    def display(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


print_handlers = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}
