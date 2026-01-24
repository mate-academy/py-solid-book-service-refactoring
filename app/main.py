from app.book import Book
from app.command_executor import CommandExecutor
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    executor = CommandExecutor(
        book=book,
        display_strategies={
            "console": ConsoleDisplay().display,
            "reverse": ReverseDisplay().display,
        },
        print_strategies={
            "console": ConsolePrinter().print_book,
            "reverse": ReversePrinter().print_book,
        },
        serializer_strategies={
            "json": JsonSerializer().serialize,
            "xml": XmlSerializer().serialize,
        },
    )

    for command, method_type in commands:
        result = executor.execute(command, method_type)
        if result is not None:
            return result

    return None
