from app.displays import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printers import PrintBook, PrintRevers
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    displays = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": PrintBook,
        "reverse": PrintRevers,
    }
    serializers = {
        "json": JSONSerializer,
        "xml": XMLSerializer
    }
    for cmd, method_type in commands:
        if cmd == "display":
            displays.get(
                method_type,
                ValueError(
                    f"There is no such display method {method_type}"
                ))().display(book)
        elif cmd == "print":
            printers.get(
                method_type,
                ValueError(
                    f"Print type {method_type} does not exist"
                ))().print(book)
        elif cmd == "serialize":
            return serializers.get(method_type)().serialize(book)


if __name__ == "__main__":
    sample_book = Book(
        "Sample Book", "This is some sample content."
    )
    print(main(
        sample_book,
        [("display", "reverse"), ("serialize", "xml")]
    ))
