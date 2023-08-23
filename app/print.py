from abc import ABC, abstractmethod

from app.book import Book


class PrintBase(ABC):
    @abstractmethod
    def get_print_type(self, book: Book, print_type: str) -> None:
        pass

    @abstractmethod
    def print_book_console(self, book: Book) -> None:
        pass

    @abstractmethod
    def print_book_reverse(self, book: Book) -> None:
        pass


class Print(PrintBase):
    def get_print_type(self, book: Book, print_type: str) -> None:
        if print_type == "console":
            self.print_book_console(book)
        elif print_type == "reverse":
            self.print_book_reverse(book)
        else:
            raise ValueError(f"Неизвестный тип печати: {print_type}")

    def print_book_console(self, book: Book) -> None:
        print(f"Печать книги: {book.title}...")
        print(book.content)

    def print_book_reverse(self, book: Book) -> None:
        print(f"Печать книги в обратном порядке: {book.title}...")
        print(book.content[::-1])
