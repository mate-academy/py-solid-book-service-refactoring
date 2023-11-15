from app.book import Book
from app.commands import DisplayCommand, SerializeCommand, PrintCommand


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_map = {
        "display": DisplayCommand,
        "print": PrintCommand,
        "serialize": SerializeCommand
    }
    for cmd, method_type in commands:
        command_class = command_map.get(cmd)
        command = command_class(method_type, book)
        return command.execute()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
