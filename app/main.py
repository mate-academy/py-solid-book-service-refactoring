from app.book import Book
from app.book_serializer import BookJSONSerializer, BookXMLSerializer
from app.book_service import BookServiceConsole, BookServiceReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service_map = {
        "console": BookServiceConsole,
        "reverse": BookServiceReverse,
    }
    serializer_map = {
        "json": BookJSONSerializer,
        "xml": BookXMLSerializer,
    }

    for cmd, method_type in commands:
        if method_type in ["console", "reverse"]:
            book_service = service_map.get(method_type)()

            match cmd:
                case "display":
                    book_service.display(book)
                case "print":
                    book_service.print_book(book)
                case _:
                    raise ValueError(f"Unknown command {cmd}")

        elif method_type in ["json", "xml"]:
            serializer = serializer_map.get(method_type)()

            match cmd:
                case "serialize":
                    return serializer.serialize(book)
                case _:
                    raise ValueError(f"Unknown command {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
