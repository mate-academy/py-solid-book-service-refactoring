from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import PrintConsole, PrintReverse
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[str]) -> None | str:
    my_registry = {
        ("display", "console"): ConsoleDisplay(),
        ("display", "reverse"): ReverseDisplay(),
        ("print", "console"): PrintConsole(),
        ("print", "reverse"): PrintReverse(),
        ("serialize", "json"): JsonSerializer(),
        ("serialize", "xml"): XmlSerializer(),
    }

    last_result = None

    for method_type in commands:
        executor = my_registry.get(method_type)
        if executor is None:
            raise ValueError(f"Unknown operation: {method_type}.")
        last_result = executor.run(book)

    return last_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, ["reverse_display", "xml_serialize"]))
