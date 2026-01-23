from app.actions import ACTIONS
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for action_name, mode in commands:
        result = ACTIONS[action_name].execute(book, mode)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
