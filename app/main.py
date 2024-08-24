from services.book.book_display import BookDisplayConsole, BookDisplayReverse
from services.book.book_print import BookPrintConsole, BookPrintReverse
from services.book.book_serialize import BookSerializeJson, BookSerializeXML


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                show_display = BookDisplayConsole()
            elif method_type == "reverse":
                show_display = BookDisplayReverse()
            else:
                raise ValueError(f"Unknown display method: {method_type}")
            show_display.display(book.content)

        elif cmd == "print":
            if method_type == "console":
                show_print = BookPrintConsole()
            elif method_type == "reverse":
                show_print = BookPrintReverse()
            else:
                raise ValueError(f"Unknown print method: {method_type}")
            show_print.print_book(book.title, book.content)

        elif cmd == "serialize":
            if method_type == "json":
                show_serialize = BookSerializeJson()
            elif method_type == "xml":
                show_serialize = BookSerializeXML()
            else:
                raise ValueError(f"Unknown serialization method:"
                                 f" {method_type}")
            return show_serialize.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
