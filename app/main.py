from app.models import Book
from app.formatters import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrinter,
    BookJSONSerializer,
    BookXMLSerializer,
    ReversePrinter,
)


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    tools = {
        ("display", "console"): ConsoleDisplay(),
        ("display", "reverse"): ReverseDisplay(),
        ("print", "console"): ConsolePrinter(),
        ("print", "reverse"): ReversePrinter(),
        ("serialize", "json"): BookJSONSerializer(),
        ("serialize", "xml"): BookXMLSerializer(),
    }

    last_result = None
    for cmd_type, method_name in commands:
        tool = tools.get((cmd_type, method_name))
        if tool:
            res = tool.execute(book)
            if res is not None:
                last_result = res

    return last_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])

    if result:
        print(result)
