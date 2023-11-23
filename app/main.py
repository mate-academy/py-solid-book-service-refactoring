from app.book import Book
from app.display import Display, ConsoleDisplay, ReverseConsoleDisplay
from app.print_book import PrintBook, ConsolePrintBook, ReversePrintBook
from app.serialize import Serialize, JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    handlers = {
        "display": lambda t: {"console": ConsoleDisplay(book),
                              "reverse": ReverseConsoleDisplay(book)}.get(t),
        "print": lambda t: {"console": ConsolePrintBook(book),
                            "reverse": ReversePrintBook(book)}.get(t),
        "serialize": lambda t: {"json": JSONSerialize(book),
                                "xml": XMLSerialize(book)}.get(t)
    }

    for cmd, method_type in commands:
        handler_creator = handlers.get(cmd)
        if handler_creator is None:
            raise ValueError(f"Command '{cmd}' is not valid.")

        handler = handler_creator(method_type)
        if handler is None:
            raise ValueError(
                f"Method type '{method_type}' not valid for command '{cmd}'.")

        if isinstance(handler, Serialize):
            return handler.serialize()
        elif isinstance(handler, PrintBook):
            handler.print_book()
        elif isinstance(handler, Display):
            handler.display()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
