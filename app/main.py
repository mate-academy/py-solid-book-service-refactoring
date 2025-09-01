from app.models import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    """
    Execute a list of commands on a Book object.
    Args:
        book: The Book instance to operate on.
        commands: A list of tuples (command, method_type), where
                  command is 'display', 'print', or 'serialize',
                  and method_type is the variant (
                  e.g.,
                  'console',
                  'reverse',
                  'json',
                  'xml'
                  ).
    Returns:
        Serialized string if 'serialize' command is executed, else None.
    """
    mapping = {
        "display": {
            "console": ConsoleDisplayer(),
            "reverse": ReverseDisplayer(),
        },
        "print": {
            "console": ConsolePrinter(),
            "reverse": ReversePrinter(),
        },
        "serialize": {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }
    }
    for cmd, method_type in commands:
        handler = mapping.get(cmd, {}).get(method_type)
        if not handler:
            raise ValueError(f"Unknown {cmd} type: {method_type}")
        if cmd == "display":
            handler.display(book)
        elif cmd == "print":
            handler.print(book)
        elif cmd == "serialize":
            return handler.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
