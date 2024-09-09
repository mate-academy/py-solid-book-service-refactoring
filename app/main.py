from app.book import Book
from app.book_processor import BookProcessor
from app.strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JSONSerialize,
    XMLSerialize
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    processor = BookProcessor(book)

    strategies = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        },
        "print": {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        },
        "serialize": {
            "json": JSONSerialize(),
            "xml": XMLSerialize(),
        },
    }

    for cmd, method_type in commands:
        if cmd == "display":
            processor.display(strategies["display"][method_type])
        elif cmd == "print":
            processor.print_book(strategies["print"][method_type])
        elif cmd == "serialize":
            return processor.serialize(strategies["serialize"][method_type])


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
