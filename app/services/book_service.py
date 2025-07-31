from app.models.book import Book
from app.strategies.display import ConsoleDisplay, ReverseDisplay
from app.strategies.print import ConsolePrint, ReversePrint
from app.strategies.serialize import JsonSerialize, XmlSerialize


class BookService:
    def __init__(self, book: Book):
        self.book = book

    def display(self, display_type: str) -> None:
        if display_type == "console":
            ConsoleDisplay().display(self.book)
        elif display_type == "reverse":
            ReverseDisplay().display(self.book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            ConsolePrint().print_book(self.book)
        elif print_type == "reverse":
            ReversePrint().print_book(self.book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return JsonSerialize().serialize(self.book)
        elif serialize_type == "xml":
            return XmlSerialize().serialize(self.book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")