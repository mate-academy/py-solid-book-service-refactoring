from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_strategy_mapping = {
        "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
        "print": {"console": ConsolePrint, "reverse": ReversePrint},
        "serialize": {"json": JsonSerializer, "xml": XmlSerializer},
    }
    for command, method_type in commands:
        try:
            strategy_class = command_strategy_mapping[command][method_type]
            strategy_instance = strategy_class(book)
            if command == "display":
                strategy_instance.display(book.content)
            elif command == "print":
                strategy_instance.print(book.content)
            elif command == "serialize":
                return strategy_instance.serialize(book.content)
        except KeyError:
            raise ValueError(f"Unknown {command} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
