from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    method_type = None

    def __init__(self, book: Book) -> None:
        pass

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintBookConsole(PrintBook):
    method_type = "console"

    def __init__(self, book: Book) -> None:
        super().__init__(book=book)
        self.message = f"Printing the book: {book.title}..."
        self.content = book.content

    def print_book(self) -> None:
        print(self.message)
        print(self.content)


class PrintBookReverse(PrintBook):
    method_type = "reverse"

    def __init__(self, book: Book, ) -> None:
        super().__init__(book=book, )
        self.message = f"Printing the book in reverse: {book.title}..."
        self.content = book.content

    def print_book(self) -> None:
        print(self.message)
        print(self.content[::-1])


def print_manager(method: str, book: Book) -> None:
    for subclass in PrintBook.__subclasses__():
        print(subclass.method_type)
        if subclass.method_type == method:
            selected_class = subclass(book=book)
            if selected_class is None:
                raise ValueError(f"Unknown print type: {method}")
            selected_class.print_book()
