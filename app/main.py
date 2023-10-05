from app.actions import ACCEPTABLE_METHODS, ACTIONS
from app.book import Book


def check_method_type(command: str, method_type: str) -> None:
    if method_type not in ACCEPTABLE_METHODS:
        raise ValueError(f"Unknown {command} type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        check_method_type(command, method_type)
        result = ACTIONS[command][method_type].do_action(book)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
