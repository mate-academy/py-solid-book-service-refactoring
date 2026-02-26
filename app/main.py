from app.book import Book
from app.command import DisplayCommand, PrintCommand, SerializeCommand


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_map = {
        "display": DisplayCommand,
        "print": PrintCommand,
        "serialize": SerializeCommand,
    }

    for cmd_name, method_type in commands:
        try:
            command = command_map[cmd_name](method_type)
        except KeyError:
            raise ValueError(f"Unknown command: {cmd_name}")

        result = command.execute(book)

        if cmd_name == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
