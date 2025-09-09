from typing import Optional

from display.console import DisplayConsole
from display.reverse import DisplayReverse
from models.book import Book
from printer.console import PrintConsole
from printer.reverse import PrintReverse
from serializer.json import SerializeJSON
from serializer.xml import SerializeXML


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = (DisplayConsole() if method_type == "console"
                         else DisplayReverse())
            displayer.display(book)
        elif cmd == "print":
            printer = (PrintConsole() if method_type == "console"
                       else PrintReverse())
            printer.print(book)
        elif cmd == "serialize":
            serializer = (SerializeJSON() if method_type == "json"
                          else SerializeXML())
            return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
