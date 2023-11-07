from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    method_type = None

    def __init__(self, book: Book) -> None:
        self.content = book.content

    @abstractmethod
    def display_book(self) -> None:
        pass


class DisplayBookConsole(DisplayBook):
    method_type = "console"

    def __init__(self, book: Book, ) -> None:
        super().__init__(book=book,)

    def display_book(self) -> None:
        print(self.content)


class DisplayBookReverse(DisplayBook):
    method_type = "reverse"

    def __init__(self, book: Book, ) -> None:
        super().__init__(book=book, )

    def display_book(self) -> None:
        print(self.content[::-1])


def display_manager(method: str, book: Book) -> None:
    for subclass in DisplayBook.__subclasses__():
        if subclass.method_type == method:
            selected_class = subclass(book=book,)
            if selected_class is None:
                raise ValueError(f"Unknown display type: {method}")
            selected_class.display_book()
