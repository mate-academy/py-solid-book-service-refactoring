from abc import ABC, abstractmethod

from app.book import Book


class DisplayBase(ABC):
    @abstractmethod
    def get_display_type(self, book: Book, display_type: str) -> None:
        pass

    @abstractmethod
    def print_console_display_type(self, book: Book) -> None:
        pass

    @abstractmethod
    def print_reverse_display_type(self, book: Book) -> None:
        pass


class Display(DisplayBase):
    def get_display_type(self, book: Book, display_type: str) -> None:
        if display_type == "console":
            self.print_console_display_type(book)
        elif display_type == "reverse":
            self.print_reverse_display_type(book)
        else:
            raise ValueError(f"Неизвестный тип отображения: {display_type}")

    def print_console_display_type(self, book: Book) -> None:
        print(book.content)

    def print_reverse_display_type(self, book: Book) -> None:
        print(book.content[::-1])
