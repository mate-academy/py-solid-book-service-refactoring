from app.book import Book
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService
from app.exceptions import DisplayTypeError, PrintTypeError, SerializeTypeError


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    try:
        for cmd, method_type in commands:
            if cmd == "display":
                display_service = DisplayService.get_display(method_type)
                display_service.display(book)
            elif cmd == "print":
                print_service = PrintService.get_print(method_type)
                print_service.print_book(book)
            elif cmd == "serialize":
                serialize_service = SerializeService.get_serialize(method_type)
                return serialize_service.serialize(book)
    except (DisplayTypeError, PrintTypeError, SerializeTypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
