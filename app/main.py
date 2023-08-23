from app.book_management.display import ConsoleDisplay, ReverseDisplay
from app.book_info.book import Book
from app.book_management.print_book import ConsolePrint, ReversePrint
from app.book_management.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    printers = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }
    serializers = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                displayers[method_type].display(book.content)
            elif cmd == "print":
                printers[method_type].print_book(book.title, book.content)
            elif cmd == "serialize":
                return serializers[method_type].serialize(
                    book.title,
                    book.content
                )
            else:
                raise ValueError
        except ValueError as e:
            print(f"{type(e).__name__}: Unknown method - {cmd}.")
        except KeyError as e:
            print(f"{type(e).__name__}: Unknown method type - {method_type}.")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "console"), ("serialize", "xml")]))
