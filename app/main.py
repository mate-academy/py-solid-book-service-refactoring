from app.book import Book
from app.utils.handlers import (Display, Print, Serialize,
                                ConsolePrint, ReversePrint)
from app.utils.display import ConsoleDisplay, ReverseDisplay
from app.utils.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_handler = get_handler_by_type(method_type, {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            })
            book.display(display_handler)
        elif cmd == "print":
            print_handler = get_handler_by_type(method_type, {
                "console": ConsolePrint(),
                "reverse": ReversePrint()
            })
            book.print_book(print_handler)
        elif cmd == "serialize":
            serialize_handler = get_handler_by_type(method_type, {
                "json": JsonSerialize(),
                "xml": XmlSerialize()
            })
            return book.serialize(serialize_handler)
        else:
            raise ValueError(f"Unknown command: {cmd}")


def get_handler_by_type(
        method_type: str,
        handler_map: dict[str, Display | Print | Serialize]
) -> Display | Print | Serialize:
    if method_type in handler_map:
        handler_instance = handler_map[method_type]
        return handler_instance
    else:
        raise ValueError(f"Unknown type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
