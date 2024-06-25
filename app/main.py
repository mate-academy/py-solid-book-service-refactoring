from app.book import Book
from app.displayers.console_display import ConsoleDisplayStrategy
from app.displayers.reverse_display import ReverseDisplayStrategy
from app.printers.console_print import ConsolePrintStrategy
from app.printers.reverse_print import ReversePrintStrategy
from app.serializers.json_serializer import JSONSerializeStrategy
from app.serializers.xml_serializer import XMLSerializeStrategy


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book
        self.display_strategies = {
            "console": ConsoleDisplayStrategy(),
            "reverse": ReverseDisplayStrategy(),
        }
        self.print_strategies = {
            "console": ConsolePrintStrategy(),
            "reverse": ReversePrintStrategy(),
        }
        self.serialize_strategies = {
            "json": JSONSerializeStrategy(),
            "xml": XMLSerializeStrategy(),
        }

    def display(self, display_type: str) -> None:
        strategy = self.display_strategies.get(display_type)
        if strategy is None:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self.book.content)

    def print_book(self, print_type: str) -> None:
        strategy = self.print_strategies.get(print_type)
        if strategy is None:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print(self.book.title, self.book.content)

    def serialize(self, serialize_type: str) -> str:
        strategy = self.serialize_strategies.get(serialize_type)
        if strategy is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self.book.title, self.book.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    for cmd, method_type in commands:
        if cmd == "display":
            service.display(method_type)
        elif cmd == "print":
            service.print_book(method_type)
        elif cmd == "serialize":
            return service.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
