from app.displays import ConsoleDisplay, ReverseDisplay
from app.exceptions import (
    DisplayException,
    PrintException,
    SerializationException
)
from app.printers import ConsolePrinter, ReversePrinter
from app.publications import Publication, Book
from app.serializers import JSONSerializer, XMLSerializer


def display_publication(display_type: str, publication: Publication) -> None:
    if display_type == "console":
        display = ConsoleDisplay()
    elif display_type == "reverse":
        display = ReverseDisplay()
    else:
        raise DisplayException(f"Unknown display type: {display_type}")

    display.display(publication)


def print_publication(print_type: str, publication: Publication) -> None:
    if print_type == "console":
        printer = ConsolePrinter()
    elif print_type == "reverse":
        printer = ReversePrinter()
    else:
        raise PrintException(f"Unknown print type: {print_type}")

    printer.print(publication)


def serialize_publication(
    serializer_type: str,
    publication: Publication
) -> str:
    if serializer_type == "json":
        serializer = JSONSerializer()
    elif serializer_type == "xml":
        serializer = XMLSerializer()
    else:
        raise SerializationException(
            f"Unknown serializer type: {serializer_type}"
        )

    return serializer.serialize(publication)


def main(
    publication: Publication,
    commands: list[tuple[str, str]]
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_publication(method_type, publication)
        elif cmd == "print":
            print_publication(method_type, publication)
        elif cmd == "serialize":
            return serialize_publication(method_type, publication)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
