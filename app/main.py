from app.book import Book
from app.display import Display, ConsoleDisplay, ReverseConsoleDisplay
from app.print_book import PrintBook, ConsolePrintBook, ReversePrintBook
from app.serialize import Serialize, JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    handlers = {
        'display': {
            'console': ConsoleDisplay(), 'reverse': ReverseConsoleDisplay()
        },
        'print': {
            'console': ConsolePrintBook(), 'reverse': ReversePrintBook()
        },
        'serialize': {'json': JSONSerialize(), 'xml': XMLSerialize()}
    }

    for cmd, method_type in commands:
        handler = handlers.get(cmd).get(method_type)
        if isinstance(handler, Serialize):
            return handler.serialize(book.title, book.content)
        elif isinstance(handler, PrintBook):
            handler.print_book(book.title, book.content)
        elif isinstance(handler, Display):
            handler.display(book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
