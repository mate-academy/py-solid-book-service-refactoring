from app.book import Book


COMMANDS = ["display", "print", "serialize"]
METHODS = ["json", "xml", "console", "reverse"]


class BookValidator:
    @classmethod
    def type_check(cls, book: Book) -> Book:
        if type(book) is not Book:
            raise TypeError("Type must be Book..")
        return book


class CommandValidator:
    @classmethod
    def command_check(
            cls, commands: list[tuple[str, str]]
    ) -> list[tuple[str, str]]:
        for cmd, method in commands:
            if cmd not in COMMANDS:
                raise ValueError(f"Unknown command: {cmd}")
            if method not in METHODS:
                raise ValueError(f"Unknown method: {method}")

        return commands
