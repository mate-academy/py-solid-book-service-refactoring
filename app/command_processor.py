from app.book import Book
from app.display_print import DisplayCommands, PrintCommands
from app.serialize import SerializerCommands


def command_processor(
        book: Book,
        command_type: DisplayCommands | PrintCommands | SerializerCommands,
        cmd_type: str,
        meth_type: str
) -> None | str:
    if meth_type == "console":
        command_type.console(book)
    elif meth_type == "reverse":
        command_type.reverse(book)
    elif meth_type == "json":
        return command_type.json(book)
    elif meth_type == "xml":
        return command_type.xml(book)
    else:
        raise ValueError(f"Unknown {cmd_type} type: {meth_type}")
