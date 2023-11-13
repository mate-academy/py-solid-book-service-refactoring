from app.book import Book
from app.display import Display, ConsoleDisplay, ReverseConsoleDisplay
from app.print_book import PrintBook, ConsolePrintBook, ReverseConsolePrintBook
from app.serialize import Serialize, JsonSerialize, XmlSerialize


DICTIONARY = {
    "display": {
        "console": ConsoleDisplay(), "reverse": ReverseConsoleDisplay()
    },
    "print": {
        "console": ConsolePrintBook(), "reverse": ReverseConsolePrintBook()
    },
    "serialize": {
        "json": JsonSerialize(), "xml": XmlSerialize()
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = DICTIONARY.get(cmd)
        if command is None:
            raise ValueError(f"Command '{cmd}' is not valid")

        method = command.get(method_type)
        if method is None:
            raise ValueError(
                f"Method type '{method_type}' is not valid for command '{cmd}'"
            )

        if isinstance(method, Display):
            method.display_func(book.content)
        elif isinstance(method, PrintBook):
            method.print_book_func(book.title, book.content)
        elif isinstance(method, Serialize):
            return method.saving_method(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
