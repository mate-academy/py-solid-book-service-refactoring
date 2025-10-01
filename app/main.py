from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import PrintConsole, PrintReverse
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            make = (ConsoleDisplay())\
                if method_type == "console" else ReverseDisplay()
            make.display(book)
        elif cmd == "print":
            make = (PrintConsole())\
                if method_type == "console" else PrintReverse()
            make.print_book(book)
        elif cmd == "serialize":
            make = (JsonSerializer())\
                if method_type == "json" else XmlSerializer()
            return make.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
