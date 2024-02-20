from app.book import Book
from app.command_processor import command_processor
from app.display_print import DisplayCommands, PrintCommands
from app.serialize import SerializerCommands


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display":
            display_commands = DisplayCommands()
            command_processor(
                book=book,
                command_type=display_commands,
                cmd_type=cmd,
                meth_type=method_type,
            )
        elif cmd == "print":
            print_commands = PrintCommands()
            command_processor(
                book=book,
                command_type=print_commands,
                cmd_type=cmd,
                meth_type=method_type,
            )

        elif cmd == "serialize":
            serializer = SerializerCommands()
            return command_processor(
                book=book,
                command_type=serializer,
                cmd_type=cmd,
                meth_type=method_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
