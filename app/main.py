from app.displayers import ReverseDisplayer, ConsoleDisplayer
from app.models import Book
from app.printers import ReversePrinter, ConsolePrinter
from app.serializers import JSONSerializer, XMLSerializer
from app.services import CommandProcessor


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    processor = CommandProcessor(
        displayers=displayers,
        printers=printers,
        serializers=serializers
    )

    return processor.process(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(f"\nSerialized Output:\n{result}")
