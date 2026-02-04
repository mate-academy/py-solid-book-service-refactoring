from app.book import Book
from app.services.display import ConsoleDisplay, ReverseDisplay
from app.services.printer import ConsolePrinter, ReversePrinter
from app.services.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    mapping = {
        "serialize":
            {
                "json": JSONSerializer,
                "xml": XMLSerializer,
            },
        "print":
            {
                "console": ConsolePrinter,
                "reverse": ReversePrinter,
            },
        "display":
            {
                "console": ConsoleDisplay,
                "reverse": ReverseDisplay,
            }
    }

    for command, process_type in commands:
        processor = mapping[command][process_type]()

        output = processor.execute(book=book)

        if command == "serialize":
            return output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(
        sample_book,
        [
            ("serialize", "json"),
            ("print", "reverse")
        ],
    ))
