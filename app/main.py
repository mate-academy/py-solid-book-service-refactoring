from app.display import ConsoleDisplay, ReverseDisplay, DisplayStrategy
from app.printer import ConsolePrint, ReversePrint, PrintStrategy
from app.serializer import JsonSerializer, XmlSerializer, SerializeStrategy


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def get_display_strategy(display_type: str) -> DisplayStrategy:
    if display_type == "console":
        return ConsoleDisplay()
    elif display_type == "reverse":
        return ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def get_print_strategy(print_type: str) -> PrintStrategy:
    if print_type == "console":
        return ConsolePrint()
    elif print_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def get_serialize_strategy(serialize_type: str) -> SerializeStrategy:
    if serialize_type == "json":
        return JsonSerializer()
    elif serialize_type == "xml":
        return XmlSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display_strategy(method_type)
            strategy.display(book.content)
        elif cmd == "print":
            strategy = get_print_strategy(method_type)
            strategy.print_book(book.title, book.content)
        elif cmd == "serialize":
            strategy = get_serialize_strategy(method_type)
            return strategy.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
