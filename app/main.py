from app.book import Book
from app.display_strategy import ConsoleDisplay, ReverseDisplay
from app.print_strategy import ConsolePrint, ReversePrint
from app.serialize_strategy import JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(), "reverse": ReverseDisplay()
    }
    print_strategies = {"console": ConsolePrint(), "reverse": ReversePrint()}
    serialize_strategies = {"json": JSONSerialize(), "xml": XMLSerialize()}

    for command, method_type in commands:
        if command == "display":
            display_strategies[method_type].display(book)
        elif command == "print":
            print_strategies[method_type].print_book(book)
        elif command == "serialize":
            return serialize_strategies[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
