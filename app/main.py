from app.managers.print_manager import PrintConsole, PrintReverse
from app.managers.serializer_manager import SerializeJSON, SerializeXML
from app.managers.display_manager import DisplayConsole, DisplayReverse
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    display_manager_dict = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse(),
    }
    print_manager_dict = {"console": PrintConsole(), "reverse": PrintReverse()}
    serialization_manager_dict = {
        "json": SerializeJSON(),
        "xml": SerializeXML()
    }

    serialized_data = ""

    for cmd, method_type in commands:

        display_manager = display_manager_dict.get(method_type)
        if display_manager:
            display_manager.display(book.content)

        print_manager = print_manager_dict.get(method_type)
        if print_manager:
            print_manager.print_book(book.title, book.content)

        serialization_manager = serialization_manager_dict.get(method_type)
        if serialization_manager:
            serialized_data = serialization_manager.serialize(
                book.title, book.content
            )

    return serialized_data


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
