from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


class BookManager:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, strategy: str) -> None:
        if strategy == "console":
            display_strategy = ConsoleDisplay()
        elif strategy == "reverse":
            display_strategy = ReverseDisplay()
        else:
            raise ValueError(f"Unknown display strategy: {strategy}")
        display_strategy.display(self.book.content)

    def print_book(self, strategy: str) -> None:
        if strategy == "console":
            print_strategy = ConsolePrinter()
        elif strategy == "reverse":
            print_strategy = ReversePrinter()
        else:
            raise ValueError(f"Unknown print strategy: {strategy}")
        print_strategy.print_book(self.book)

    def serialize(self, strategy: str) -> str:
        if strategy == "json":
            serializer = JsonSerializer()
        elif strategy == "xml":
            serializer = XmlSerializer()
        else:
            raise ValueError(f"Unknown serialize strategy: {strategy}")
        return serializer.serialize(self.book)
