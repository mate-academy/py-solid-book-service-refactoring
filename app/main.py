from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import PrintConsole, PrintReverse
from app.serializers import JsonSerializer, XmlSerializer
from app.registry import registry


registry.register("display", "console", ConsoleDisplay())
registry.register("display", "reverse", ReverseDisplay())
registry.register("print", "console", PrintConsole())
registry.register("print", "reverse", PrintReverse())
registry.register("serialize", "json", JsonSerializer())
registry.register("serialize", "xml", XmlSerializer())


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    last_result = None

    for cmd_type, method_type in commands:
        executor = registry.get_executor(cmd_type, method_type)

        if executor is None:
            raise ValueError(f"Unknown operation: {cmd_type} {method_type}")

        if hasattr(executor, "display"):
            executor.display(book)
        elif hasattr(executor, "serialize"):
            last_result = executor.serialize(book)

    return last_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse")]))
