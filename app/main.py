from app.book import Book
from app.utils.utils import get_handler_by_type
from app.utils.display import ConsoleDisplay, ReverseDisplay

from enum import Enum


class Command(Enum):
    DISPLAY = "display"

    @property
    def handlers_dict(self) -> dict[str, callable]:
        commands_info = {
            Command.DISPLAY: {
                "console": lambda: ConsoleDisplay(),
                "reverse": lambda: ReverseDisplay()
            }
        }

        return commands_info.get(self, {})

    def get_book_method(self, book: Book) -> callable:
        methods = {
            Command.DISPLAY: book.display
        }

        return methods.get(self)

    def invoke(self, book: Book, method_type: str) -> None:
        method = self.get_book_method(book)
        handler = get_handler_by_type(method_type, self.handlers_dict)

        method(handler)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = Command(cmd)
        return command.invoke(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
