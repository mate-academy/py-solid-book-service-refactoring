from .book import Book
from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrinter, ReversePrinter
from .serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = (
                ConsoleDisplay()
                if method_type == "console"
                else ReverseDisplay()
            )
            strategy.display(book)
        elif cmd == "print":
            strategy = (
                ConsolePrinter()
                if method_type == "console"
                else ReversePrinter()
            )
            strategy.print(book)
        elif cmd == "serialize":
            strategy = (
                JsonSerializer() if method_type == "json" else XmlSerializer()
            )
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
