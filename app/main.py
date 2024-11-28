from book.book import Book
from book.book_print import PrintBookConsole, PrintBookReverse
from book.book_display import DisplayBookConsole, DisplayBookReverse
from book.book_serialize import SerializeBookJson, SerializeBookXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_console = DisplayBookConsole()
                display_console.display(book)
            if method_type == "reverse":
                display_reverse = DisplayBookReverse()
                display_reverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                print_console = PrintBookConsole()
                print_console.print_book(book)
            if method_type == "reverse":
                print_reverse = PrintBookReverse()
                print_reverse.print_book(book)
        elif cmd == "serialize":
            if method_type == "xml":
                xml_serialize = SerializeBookXml()
                return xml_serialize.serialize(book)
            if method_type == "json":
                json_serialize = SerializeBookJson()
                return json_serialize.serialize(book)
        else:
            raise ValueError("Unknown data type")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
