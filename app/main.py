from app.book import Book
from app.display import ConsoleDisplayStrategy, ReverseDisplayStrategy
from app.print_book import ConsolePrintStrategy, ReversePrintStrategy
from app.serialize import JSONSerializeStrategy, XMLSerializeStrategy


class BookProcessor:
    def __init__(self, book: Book) -> None:
        self.book = book

    def process(self, commands: list[tuple[str, str]]) -> None | str:
        for cmd, method_type in commands:
            if cmd == "display":
                self._process_display(method_type)
            elif cmd == "print":
                self._process_print(method_type)
            elif cmd == "serialize":
                return self._process_serialize(method_type)

    def _process_display(self, method_type: str) -> None:
        if method_type == "console":
            strategy = ConsoleDisplayStrategy()
        elif method_type == "reverse":
            strategy = ReverseDisplayStrategy()
        else:
            raise ValueError(f"Unknown display type: {method_type}")
        strategy.display(self.book)

    def _process_print(self, method_type: str) -> None:
        if method_type == "console":
            strategy = ConsolePrintStrategy()
        elif method_type == "reverse":
            strategy = ReversePrintStrategy()
        else:
            raise ValueError(f"Unknown print type: {method_type}")
        strategy.print_book(self.book)

    def _process_serialize(self, method_type: str) -> str:
        if method_type == "json":
            strategy = JSONSerializeStrategy()
        elif method_type == "xml":
            strategy = XMLSerializeStrategy()
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return strategy.serialize(self.book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    processor = BookProcessor(book)
    return processor.process(commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
