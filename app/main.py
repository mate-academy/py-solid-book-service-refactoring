from typing import Union

from app.book import Book
from app.manager import DISPLAY, PRINT, SERIALIZE
from app.print import ConsolePrint, ReversePrint


def main(book: Book, commands: list[tuple[str, str]]) -> Union[None, str]:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY[method_type]().display(book.content)
        if cmd == "print":
            PRINT[method_type]().print(book.title, book.content)
        if cmd == "serialize":
            return SERIALIZE[method_type]().serialize(book)


class PrintStrategyFactory:
    @staticmethod
    def get_strategy(print_type: str) -> Union[ConsolePrint, ReversePrint]:
        if print_type == "console":
            return ConsolePrint()
        if print_type == "reverse":
            return ReversePrint()
        raise ValueError(f"Unknown print type: {print_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
