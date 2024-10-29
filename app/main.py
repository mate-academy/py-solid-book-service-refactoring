from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = ConsoleDisplay()\
                if method_type == "console"else ReverseDisplay()
            display_strategy.display(book.content)
        elif cmd == "print":
            printer = ConsolePrinter()\
                if method_type == "console" else ReversePrinter()
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = JsonSerializer()\
                if method_type == "json" else XmlSerializer()
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
