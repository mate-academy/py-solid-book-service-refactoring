from app.book import Book
from app.command import Command, Action, Mode, COMMAND_FACTORY


def main(book: Book, actions: list[tuple[str, str]]) -> None | str:
    commands: list[Command] = []

    for action_str, mode_str in actions:
        action = Action(action_str)
        mode = Mode(mode_str)
        commands.append(COMMAND_FACTORY[(action, mode)](book))

    for cmd in commands:
        result = cmd.execute()
        if result is not None:
            return result

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
