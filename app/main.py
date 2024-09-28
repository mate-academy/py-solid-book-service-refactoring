from app.book import Book
from app.command_factories import (
    DisplayCommands,
    PrintCommands,
    SerializerCommands
)


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> None | str:
    context = book.get_context()
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayCommands().create_command_class(
                method_type
            ).display(context["text"])
        elif cmd == "print":
            PrintCommands().create_command_class(
                method_type
            ).print_entity(context)
        elif cmd == "serialize":
            return SerializerCommands().create_command_class(
                method_type
            ).convert_data(context)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
