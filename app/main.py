from app.book import Book
from app.display_strategy import ConsoleDisplay, ReverseDisplay
from app.print_strategy import ConsolePrint, ReversePrint
from app.serialize_strategy import JsonSerializer, XmlSerializer
from app.book_manager import BookManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    strategies = {
        "display": {"console": ConsoleDisplay(), "reverse": ReverseDisplay()},
        "print": {"console": ConsolePrint(), "reverse": ReversePrint()},
        "serialize": {"json": JsonSerializer(), "xml": XmlSerializer()},
    }
    for cmd, method_type in commands:
        if cmd in strategies and method_type in strategies[cmd]:
            strategy = strategies[cmd][method_type]
            manager = BookManager(
                book,
                strategy if cmd == "display" else None,
                strategy if cmd == "print" else None,
                strategy if cmd == "serialize" else None
            )
            if cmd == "display":
                manager.display()
            elif cmd == "print":
                manager.print_book()
            elif cmd == "serialize":
                return manager.serialize()
        else:
            raise ValueError(f"Unknown {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
