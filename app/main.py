from app.book import Book, DisplayBook, PrintBook
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_action = DisplayBook(method_type)
            book_action.action(book)
        if cmd == "print":
            book_action = PrintBook(method_type)
            book_action.action(book)
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer(book)
            elif method_type == "xml":
                serializer = XmlSerializer(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
