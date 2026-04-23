from app.book import Book
from app.bookdisplayer import BookDisplayer
from app.bookprinter import BookPrinter
from app.formatter import ReverseFormatter, ConsolFormatter
from app.serialzers import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    formatters = {
        "console": ConsolFormatter(),
        "reverse": ReverseFormatter()
    }

    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    results = None

    for cmd, method_type in commands:
        formatter = formatters.get(method_type)

        if cmd == "display":
            BookDisplayer().display(book, formatter)

        elif cmd == "print":
            BookPrinter().print_book(book, formatter)

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            results = serializer.serialize(book)

    return results
