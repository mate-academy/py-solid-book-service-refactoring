import abc

from app.book import Book
from app.book_display import BookDisplayConsole, BookDisplayReverse
from app.book_print import BookPrintConsole, BookPrintReverse
from app.serializer import JSONSerializer, XMLSerializer


def input_commands(cmd: str, method_type: str) -> abc.ABCMeta:
    if cmd == "display":
        display_mapping = {
            "console": BookDisplayConsole,
            "reverse": BookDisplayReverse,
        }

        return display_mapping.get(method_type)

    elif cmd == "print":
        print_mapping = {
            "console": BookPrintConsole,
            "reverse": BookPrintReverse,
        }

        return print_mapping.get(method_type)

    elif cmd == "serialize":
        serializer_mapping = {
            "json": JSONSerializer,
            "xml": XMLSerializer,
        }

        return serializer_mapping.get(method_type)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        current_command = input_commands(cmd, method_type)

        return current_command(book).execute()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
