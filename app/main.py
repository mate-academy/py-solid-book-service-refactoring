from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = ConsoleDisplay()\
                if method_type == "console"\
                else ReverseDisplay()
            display_strategy.display(book)
        elif cmd == "print":
            print_strategy = ConsolePrint()\
                if method_type == "console"\
                else ReversePrint()
            print_strategy.print_book(book)
        elif cmd == "serialize":
            serializer = JsonSerializer()\
                if method_type == "json"\
                else XmlSerializer()
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
