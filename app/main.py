from app.services import BookCommandService
from app.enums import Command
from app.models import Book


def main(book: "Book", commands: list[tuple[str, str]]) -> None | str:
    service = BookCommandService()

    for cmd, method_type in commands:
        cmd_enum = Command.from_str(cmd)
        match cmd_enum:
            case Command.DISPLAY:
                service.display(book, method_type)
            case Command.PRINT:
                service.print(book, method_type)
            case Command.SERIALIZE:
                return service.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
