from app.display_types import ConsoleDisplayBook, ReverseDisplayBook
from app.print_types import ConsolePrintBook, ReversePrintBook
from app.serializers import JsonSerializer, XmlSerializer

COMMANDS = {
    "display": {
        "console": ConsoleDisplayBook.display_book_content,
        "reverse": ReverseDisplayBook.display_book_content,
    },
    "print": {
        "console": ConsolePrintBook.print_book,
        "reverse": ReversePrintBook.print_book,
    },
    "serialize": {
        "json": JsonSerializer.serialize,
        "xml": XmlSerializer.serialize,
    }
}
