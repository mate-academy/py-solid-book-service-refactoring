from app.displayers import Displayer, Printer
from app.formatters import ConsoleFormatter, ReverseFormatter
from app.serializers import JsonSerializer, XmlSerializer


FORMATTERS = {
    "console": ConsoleFormatter,
    "reverse": ReverseFormatter,
}

SERIALIZERS = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def _handle_display(book: Book, method_type: str) -> None:
    formatter_class = FORMATTERS.get(method_type)
    if not formatter_class:
        raise ValueError(f"Unknown display type: {method_type}")
    displayer = Displayer(formatter_class())
    displayer.display(book.content)


def _handle_print(book: Book, method_type: str) -> None:
    formatter_class = FORMATTERS.get(method_type)
    if not formatter_class:
        raise ValueError(f"Unknown print type: {method_type}")
    printer = Printer(formatter_class())
    printer.print(book.title, book.content)


def _handle_serialize(book: Book, method_type: str) -> str:
    serializer_class = SERIALIZERS.get(method_type)
    if not serializer_class:
        raise ValueError(f"Unknown serialize type: {method_type}")
    serializer = serializer_class()
    return serializer.serialize(book.title, book.content)


COMMANDS = {
    "display": _handle_display,
    "print": _handle_print,
    "serialize": _handle_serialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        handler = COMMANDS.get(cmd)
        if not handler:
            raise ValueError(f"Unknown command: {cmd}")
        result = handler(book, method_type)
        if cmd == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
