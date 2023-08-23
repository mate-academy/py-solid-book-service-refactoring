from app.book import Book


COMMANDS_LIST = ["display", "print", "serialize"]
METHODS_LIST = ["json", "xml", "console", "reverse"]


class BookTypeValidator:

    @classmethod
    def type_checker(cls, book: Book) -> Book:
        if type(book) is not Book:
            raise TypeError("Wrong type")
        return book


class CommandsValidator:
    @classmethod
    def commands_checker(
            cls, commands: list[tuple[str, str]]
    ) -> list[tuple[str, str]]:
        for cmd, method_type in commands:
            if cmd not in COMMANDS_LIST:
                raise ValueError(f"Unknown command: {cmd}")
            if method_type not in METHODS_LIST:
                raise ValueError(f"Unknown method type: {method_type}")
        return commands
