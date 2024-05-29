from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display = DisplayConsole(book)
                display.display()
            else:
                display = DisplayReverse(book)
                display.display()
        elif cmd == "print":
            if method_type == "console":
                print_console = PrintConsole(book)
                print_console.print()
            else:
                print_reverse = PrintReverse(book)
                print_reverse.print()
        elif cmd == "serialize":
            if method_type == "json":
                serialize = SerializeJson(book)
                return serialize.serialize()
            else:
                serialize = SerializeXml(book)
                return serialize.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
