from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class BookAction(ABC):
    @abstractmethod
    def action(self, book: Book) -> None:
        pass


class DisplayBook(BookAction):
    def __init__(self, display_type: str):
        self.display_type = display_type

    def action(self, book: Book) -> None:
        if self.display_type == "console":
            print(book.content)
        elif self.display_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {self.display_type}")


class PrintBook(BookAction):
    def __init__(self, print_type: str):
        self.print_type = print_type

    def action(self, book: Book) -> None:
        if self.print_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif self.print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {self.print_type}")
