from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonBookSerializer, XmlBookSerializer


class BookService:
    def __init__(self, book: Book, cmd: str, method: str) -> None:
        self.book = book
        self.method_name = f"{cmd}_{method}"
        self.act = getattr(self, self.method_name, None)
        if not callable(self.act):
            raise AttributeError(
                f"Method '{self.method_name}' not found or is not callable."
            )

    def display_console(self) -> None:
        return ConsoleDisplay().display(self.book.content)

    def display_reverse(self) -> None:
        return ReverseDisplay().display(self.book.content)

    def print_console(self) -> None:
        return ConsolePrint().print_book(self.book.title, self.book.content)

    def print_reverse(self) -> None:
        return ReversePrint().print_book(self.book.title, self.book.content)

    def serialize_json(self) -> str:
        return JsonBookSerializer().serialize(
            self.book.title, self.book.content)

    def serialize_xml(self) -> str:
        return XmlBookSerializer().serialize(
            self.book.title, self.book.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        act = BookService(book, cmd, method_type)
        return act.act()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
