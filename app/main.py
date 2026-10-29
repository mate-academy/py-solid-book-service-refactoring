from app.display import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer

DISPLAYS = {"console": ConsoleDisplay, "reverse": ReverseDisplay}
PRINTERS = {"console": ConsolePrinter, "reverse": ReversePrinter}
SERIALIZERS = {"json": JsonSerializer, "xml": XmlSerializer}


def create(registry: dict, key: str, kind: str) -> None:
    if key not in registry:
        raise ValueError(f"Unknown {kind} type: {key}")
    return registry[key]()


def run_display(book: Book, method_type: str) -> None:
    create(DISPLAYS, method_type, "display").display(book)


def run_print(book: Book, method_type: str) -> None:
    create(PRINTERS, method_type, "print").print_book(book)


def run_serialize(book: Book, method_type: str) -> str:
    return create(SERIALIZERS, method_type, "serialize").serialize(book)


ACTIONS = {"display": run_display, "print": run_print}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "serialize":
            return run_serialize(book, method_type)
        action = ACTIONS.get(cmd)
        if action:
            action(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
