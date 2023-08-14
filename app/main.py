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

    for cmd, method_type in commands:
        if cmd == "display":
            display_manager = display_manager.get(method_type)
            if display_manager:
                display_manager.display(book.content)
        elif cmd == "print":
            print_manager = print_manager.get(method_type)
            if print_manager:
                print_manager.print(book.title, book.content)
        elif cmd == "serialize":
            serialization_manager = serialization_manager.get(method_type)
            if serialization_manager:
                result = serialization_manager.serialize(
                    book.title, book.content
                )

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
