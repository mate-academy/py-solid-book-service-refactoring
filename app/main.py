from typing import Optional

from app.models import Book
from app.actions import ActionRegistry


def main(book: Book, commands: list) -> Optional[str]:
    for cmd, method_type in commands:
        action = ActionRegistry.get_action(cmd)
        result = action.execute(book, method_type)

        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
