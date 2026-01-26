from app.services import BookCommandService
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService
from app.enums import Command, DisplayType, PrintType, SerializeType
from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def create_book_command_service() -> BookCommandService:
    """Composition root - wire up all dependencies"""
    displays = {
        DisplayType.CONSOLE: ConsoleDisplay(),
        DisplayType.REVERSE: ReverseDisplay(),
    }

    printers = {
        PrintType.CONSOLE: ConsolePrinter(),
        PrintType.REVERSE: ReversePrinter(),
    }

    serializers = {
        SerializeType.JSON: JsonSerializer(),
        SerializeType.XML: XmlSerializer(),
    }

    display_service = DisplayService(displays)
    print_service = PrintService(printers)
    serialize_service = SerializeService(serializers)

    return BookCommandService(
        display_service,
        print_service,
        serialize_service
    )


def main(
        book: Book,
        commands: list[tuple[str, str]],
        service: BookCommandService = None
) -> None | str:
    if service is None:
        service = create_book_command_service()

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
    print(
        main(
            sample_book, [("display", "reverse"), ("serialize", "xml")]
        )
    )
