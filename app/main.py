from app.book import Book
from app.utils.handlers import (Display,
                                Print,
                                ConsoleDisplay,
                                ReverseDisplay,
                                ConsolePrint,
                                ReversePrint
                                )
from app.utils.serializers import Serialize, JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_handler = get_handler_by_type(method_type, {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            })
            display_handler.display(book.content)
        elif cmd == "print":
            print_handler = get_handler_by_type(method_type, {
                "console": ConsolePrint(),
                "reverse": ReversePrint()
            })
            print_handler.print(book.title, book.content)
        elif cmd == "serialize":
            serialize_handler = get_handler_by_type(method_type, {
                "json": JsonSerialize(),
                "xml": XmlSerialize()
            })
            return serialize_handler.serialize(book.title, book.content)
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
