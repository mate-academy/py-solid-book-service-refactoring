from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.printer import ConsolePrinterBook, ReversePrinterBook
from app.serializer import JSONSerializeBook, XMLSerializeBook
from book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    handler_dict = {
        "display": {
            "console": ConsoleDisplayBook.display,
            "reverse": ReverseDisplayBook.display,
        },
        "print": {
            "console": ConsolePrinterBook.print_book,
            "reverse": ReversePrinterBook.print_book,
        },
        "serialize": {
            "json": JSONSerializeBook.serialize,
            "xml": XMLSerializeBook.serialize
        }
    }

    for cmd, method_type in commands:
        if cmd in handler_dict:
            if method_type in handler_dict[cmd]:
                return handler_dict[cmd][method_type](book)
            raise ValueError(f"Unknown {cmd} type: {method_type}")
        raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    # print(main(sample_book, [("print", "reverse"), ("serialize", "xml")]))
    print(main(sample_book, [("serialize", "json")]))
