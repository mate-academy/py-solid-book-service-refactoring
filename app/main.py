from enum import Enum
from typing import Union, Callable, Dict

from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrinter, ReversePrinter
from app.serializer import XMLSerializer, JSONSerializer

from app.solid import Book, ConsoleFormatter, ReverseFormatter


class CommandType(Enum):
    DISPLAY = "display"
    PRINT = "print"
    SERIALIZE = "serialize"


class MethodType(Enum):
    CONSOLE = "console"
    REVERSE = "reverse"
    JSON = "json"
    XML = "xml"


STRATEGIES: Dict[tuple[CommandType, MethodType], Callable] = {
    (CommandType.DISPLAY, MethodType.CONSOLE):
        lambda b: ConsoleDisplay(b, ConsoleFormatter()).display(),
    (CommandType.DISPLAY, MethodType.REVERSE):
        lambda b: ReverseDisplay(b, ReverseFormatter()).display(),
    (CommandType.PRINT, MethodType.CONSOLE):
        lambda b: ConsolePrinter(b, ConsoleFormatter()).print(),
    (CommandType.PRINT, MethodType.REVERSE):
        lambda b: ReversePrinter(b, ReverseFormatter()).print(),
    (CommandType.SERIALIZE, MethodType.JSON):
        lambda b: JSONSerializer().serialize(b.title, b.content),
    (CommandType.SERIALIZE, MethodType.XML):
        lambda b: XMLSerializer().serialize(b.title, b.content),
}


def main(book: Book, commands: list[tuple[str, str]]) -> Union[None | str]:
    result = None
    for cmd_str, method_str in commands:
        try:
            cmd_type = CommandType(cmd_str)
            method_type = MethodType(method_str)
        except ValueError:
            continue
        action = STRATEGIES.get((cmd_type, method_type))
        if action:
            res = action(book)
            if res is not None:
                result = res

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
