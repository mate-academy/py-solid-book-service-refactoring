from app.book.book_model import Book
from app.display.display_build import DisplayBuild
from app.print.print_build import PrintBuild
from app.serialize.serialize_build import SerializeBuild


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def process_commands(self, commands: list[tuple[str, str]]) -> None | str:
        result = None

        for cmd, method_type in commands:
            if cmd == "display":
                build = DisplayBuild.display_build(method_type)
                result = build.display(self.book)
            elif cmd == "print":
                build = PrintBuild.print_build(method_type)
                result = build.print_book(self.book)
            elif cmd == "serialize":
                build = SerializeBuild.serialize_build(method_type)
                result = build.serialize(self.book)

        return result
