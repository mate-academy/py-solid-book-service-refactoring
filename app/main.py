from app.book import Book
from app.print import ConsolePrint, ReversePrint
from app.display import ReverseDisplay, ConsoleDisplay
from app.serializers import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialization_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            book.apply_display_strategy(display_strategies[method_type])
        elif cmd == "print":
            book.apply_print_strategy(print_strategies[method_type])
        elif cmd == "serialize":
            result = book.apply_serialization_strategy(
                serialization_strategies[method_type]
            )

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
