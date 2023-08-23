from app.book import Book
from app.display import DisplayBook
from app.print import PrintBook
from app.serializer import SerializerBook


COMMANDS_LIST = ["display.py", "print", "serialize"]
METHODS_LIST = ["json", "xml", "console", "reverse"]


class BookManager:
    def __init__(self, book: Book, commands: list[tuple[str, str]]) -> None:
        self.book = self.type_checker(book)
        self.commands = self.commands_checker(commands)
        self.performer_actions()

    @classmethod
    def type_checker(cls, book) -> Book:
        if type(book) is not Book:
            raise TypeError("Wrong type")
        return book

    @classmethod
    def commands_checker(cls, commands: list[tuple[str, str]]) -> list[tuple[str, str]]:
        for cmd, method_type in commands:
            if cmd not in COMMANDS_LIST:
                raise ValueError(f"Unknown command: {cmd}")
            if method_type not in METHODS_LIST:
                raise ValueError(f"Unknown method type: {method_type}")
        return commands

    def performer_actions(self) -> None | str:
        for cmd, method_type in self.commands:
            if cmd == "display.py":
                display_book = DisplayBook(self.book, method_type)
                display_book.display()
            elif cmd == "print":
                print_book = PrintBook(self.book, method_type)
                print_book.print_book()
            elif cmd == "serialize":
                serializer_book = SerializerBook(self.book, method_type)
                return serializer_book.serialize()
