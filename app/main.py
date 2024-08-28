from book.book_display import DisplayBook
from book.book_print import PrintBook
from book.book_serializer import SerializeBook
from book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book = DisplayBook(book)
            if method_type == "console":
                display_book.display_console()
            elif method_type == "reverse":
                display_book.display_reverse()
        elif cmd == "print":
            print_book = PrintBook(book)
            if method_type == "console":
                print_book.print_console()
            elif method_type == "reverse":
                print_book.print_reverse()
        elif cmd == "serialize":
            serializer_book = SerializeBook(book)
            if method_type == "json":
                return serializer_book.serialize_json()
            return serializer_book.serialize_xml()
