from app.book import Book, PrintBook, Display
from app.serializer import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Display(method_type)
            if method_type == "console":
                display.console(book)
            elif method_type == "reverse":
                display.reverse(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            print_book = PrintBook(method_type)
            if method_type == "console":
                print_book.console(book)
            elif method_type == "reverse":
                print_book.reverse(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            json = SerializeJson(method_type)
            xml = SerializeXml(method_type)
            if method_type == "json":
                return json.serialize_json(book)
            elif method_type == "xml":
                return xml.serialize_xml(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
