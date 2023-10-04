from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializeJSON, SerializeXML

DISPLAY = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}
PRINT_BOOK = {
    "console": PrintConsole,
    "reverse": PrintReverse,
}
SERIALIZE = {
    "json": SerializeJSON,
    "xml": SerializeXML,
}
ACCEPTABLE_METHODS = {*DISPLAY.keys(), *PRINT_BOOK.keys(), *SERIALIZE.keys()}


def check_method_type(command: str, method_type: str) -> None:
    if method_type not in ACCEPTABLE_METHODS:
        raise ValueError(f"Unknown {command} type: {method_type}")


def check_command(book: Book, command: str, method_type: str) -> None | str:
    if command == "display":
        DISPLAY[method_type].do_action(book)
    elif command == "print":
        PRINT_BOOK[method_type].do_action(book)
    elif command == "serialize":
        return SERIALIZE[method_type].do_action(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        check_method_type(command, method_type)
        result = check_command(book, command, method_type)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
