from app.book_implementation import Book
from app.print_manage import ConsolePrint, ReversePrint
from app.serializer_manage import XmlBookSerialize, JsonBookSerialize
from app.display_manage import ConsoleDisplay, ReverseDisplay


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display
        },
        "print": {
            "console": ConsolePrint.print_book,
            "reverse": ReversePrint.print_book
        },
        "serialize": {
            "json": JsonBookSerialize.serialize_book,
            "xml": XmlBookSerialize.serialize_book
        }
    }
    for cmd, method_type in commands:
        if cmd in actions and method_type in actions[cmd]:
            method = actions[cmd][method_type]
            return method(book)
        else:
            raise ValueError(f"Unknown command or method type")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
