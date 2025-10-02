from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import BookPrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {"console": ConsoleDisplayer(), "reverse": ReverseDisplayer()}

    printers = {
        "console": BookPrinter(ConsoleDisplayer()),
        "reverse": BookPrinter(ReverseDisplayer()),
    }

    serializers = {"json": JsonSerializer(), "xml": XmlSerializer()}

    for cmd, method_type in commands:
        if cmd == "display":
            displayers[method_type].display(book)
        elif cmd == "print":
            printers[method_type].print_book(book)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
