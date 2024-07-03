from app.book import Book
from app.display_strategy import DisplayStrategy
from app.print_strategy import PrintStrategy
from app.serialize_strategy import SerializeStrategy


class BookManager:
    def __init__(
            self,
            book: Book,
            display_strategy: DisplayStrategy = None,
            print_strategy: PrintStrategy = None,
            serialize_strategy: SerializeStrategy = None
    ) -> None:
        self.book = book
        self.display_strategy = display_strategy
        self.print_strategy = print_strategy
        self.serialize_strategy = serialize_strategy

    def display(self) -> None:
        if self.display_strategy:
            self.display_strategy.display(self.book.content)

    def print_book(self) -> None:
        if self.print_strategy:
            self.print_strategy.print(self.book.title, self.book.content)

    def serialize(self) -> str:
        if self.serialize_strategy:
            return self.serialize_strategy.serialize(self.book)
