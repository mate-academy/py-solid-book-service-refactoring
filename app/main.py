from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ReversePrint, ConsolePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_handlers = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    print_handlers = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serialize_handlers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            handler_display = display_handlers.get(method_type)
            if not handler_display:
                raise ValueError(f"Unknown type: {method_type}")
            handler_display.display(book)

        elif cmd == "print":
            handler_print = print_handlers.get(method_type)
            if not handler_print:
                raise ValueError(f"Unknown type: {method_type}")
            handler_print.print_book(book)

        elif cmd == "serialize":
            handler_serialize = serialize_handlers.get(method_type)
            if not handler_serialize:
                raise ValueError(f"Unknown type: {method_type}")

            return handler_serialize.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
