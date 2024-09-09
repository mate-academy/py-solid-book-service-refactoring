from app.book import Book
from app.strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JSONSerialize,
    XMLSerialize
)


class BookProcessor:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self,
                display_strategy: ConsoleDisplay | ReverseDisplay) -> None:
        display_strategy.display(self.book.content)

    def print_book(self,
                   print_strategy: ConsolePrint | ReversePrint) -> None:
        print_strategy.print_book(self.book.title, self.book.content)

    def serialize(self,
                  serialize_strategy: JSONSerialize | XMLSerialize) -> str:
        return serialize_strategy.serialize(self.book.title, self.book.content)
