from app.book import Book
from app.serializer import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            if method_type == "json":
                serializer = SerializeJson(method_type)
                return serializer.serialize_json(book)
            elif method_type == "xml":
                serializer = SerializeXml(method_type)
                return serializer.serialize_xml(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
