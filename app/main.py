from app.books import Book
from app.display import ConsoleDisplayService, ReverseDisplayService
from app.print import ConsolePrintService, ReversePrintService
from app.serializer import JsonSerializer, XmlSerializer

DISPATCHER = {
    "display": {
        "console": ConsoleDisplayService.display,
        "reverse": ReverseDisplayService.display,
        "must_return_value": False
    },
    "print": {
        "console": ConsolePrintService.print,
        "reverse": ReversePrintService.print,
        "must_return_value": False
    },
    "serialize": {
        "json": JsonSerializer.serialize,
        "xml": XmlSerializer.serialize,
        "must_return_value": True
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in DISPATCHER and method_type in DISPATCHER[cmd]:
            result = DISPATCHER[cmd][method_type](book)
            if DISPATCHER[cmd].get("must_return_value"):
                return result
        else:
            raise ValueError(f"Unknown {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "json")]))
    print(main(sample_book, [("print", "console"), ("serialize", "xml")]))
