from app.book import Book
from app.display import DisplayFactory
from app.print import PrintFactory
from app.serializer import SerializerFactory
from app.errors import UnknownCommandError


class CommandHandler:
    def __init__(self) -> None:
        self.command_map = {
            "display": DisplayFactory,
            "print": PrintFactory,
            "serialize": SerializerFactory
        }

    def execute(self, book: Book, cmd: str, method_type: str) -> None | str:
        if cmd not in self.command_map:
            raise UnknownCommandError(cmd)

        factory = self.command_map[cmd]

        if cmd == "display":
            factory.create_display(method_type).display(book.content)
        elif cmd == "print":
            factory.create_print(method_type).print(book.title, book.content)
        elif cmd == "serialize":
            return factory.create_serializer(method_type).serialize(
                book.title, book.content
            )
