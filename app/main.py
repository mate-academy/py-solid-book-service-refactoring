from app.book import Book
from app.managers.display_manager import DisplayConsole, DisplayReverse
from app.managers.print_manager import PrintConsole, PrintReverse
from app.managers.serialize_manager import SerializeJSON, SerializeXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_manager = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse(),
    }
    print_manager = {"console": PrintConsole(), "reverse": PrintReverse()}
    serialization_manager = {"json": SerializeJSON(), "xml": SerializeXML()}

    result = ""

    command_functions = {
        "display": lambda method_type: display_manager.get(
            method_type
        ).display(book.content)
        if display_manager.get(method_type)
        else None,
        "print": lambda method_type: print_manager.get(method_type).print(
            book.title, book.content
        )
        if print_manager.get(method_type)
        else None,
        "serialize": lambda method_type: serialization_manager.get(
            method_type
        ).serialize(book.title, book.content)
        if serialization_manager.get(method_type)
        else None,
    }

    for cmd, method_type in commands:
        if cmd in command_functions:
            result = command_functions[cmd](method_type) or result

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
