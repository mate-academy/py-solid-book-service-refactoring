from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import SerializerJSON, SerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    }
    serializers = {
        "json": SerializerJSON,
        "xml": SerializerXML,
    }
    all_method_types = (
        list(displays.keys())
        + list(printers.keys())
        + list(serializers.keys())
    )
    for cmd, method_type in commands:
        if method_type not in all_method_types:
            raise ValueError(f"Unknown method entered: {method_type}.")

        if cmd == "display":
            displays[method_type]().perform_display(book)
        elif cmd == "print":
            printers[method_type]().perform_print(book)
        elif cmd == "serialize":
            return serializers[method_type]().perform_serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
