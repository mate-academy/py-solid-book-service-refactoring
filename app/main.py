from app.book import Book
from app.display import ConsoleDisplay
from app.formater import NormalFormat, ReverseFormat
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                formatter = NormalFormat()
            elif method_type == "reverse":
                formatter = ReverseFormat()
            else:
                raise ValueError(f"Unknown display type: {method_type}")

            display = ConsoleDisplay(formatter)
            display.display(book)

        elif cmd == "print":
            if method_type == "console":
                formatter = NormalFormat()
                print(f"Printing the book: {book.title}...")
            elif method_type == "reverse":
                formatter = ReverseFormat()
                print(f"Printing the book in reverse: {book.title}...")
            print(formatter.format(book))

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serialize method: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
