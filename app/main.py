from services.book.BookDisplay import BookDisplayConsole, BookDisplayReverse
from services.book.BookPrint import BookPrintConsole, BookPrintReverse
from services.book.BookSerialize import BookSerializeJson, BookSerializeXML


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                show_display = BookDisplayConsole(book)
            elif method_type == "reverse":
                show_display = BookDisplayReverse(book)
            else:
                raise ValueError(f"Unknown display method: {method_type}")
            show_display.display()

        elif cmd == "print":
            if method_type == "console":
                show_print = BookPrintConsole(book)
            elif method_type == "reverse":
                show_print = BookPrintReverse(book)
            else:
                raise ValueError(f"Unknown print method: {method_type}")
            show_print.print_book()

        elif cmd == "serialize":
            if method_type == "json":
                show_serialize = BookSerializeJson(book)
            elif method_type == "xml":
                show_serialize = BookSerializeXML(book)
            else:
                raise ValueError(f"Unknown serialization method:"
                                 f" {method_type}")
            return show_serialize.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
