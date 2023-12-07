from .book import BookABC
from .display import DisplayInReverse, DisplayToConsole
from .printer import PrinterInReverse, PrinterToConsole
from .serializer import SerializeToJSON, SerializeToXML

EXECUTE = {
    "display": {
        "console": DisplayToConsole.display,
        "reverse": DisplayInReverse.display,
    },
    "print": {
        "console": PrinterToConsole.print_book,
        "reverse": PrinterInReverse.print_book,
    },
    "serialize": {
        "json": SerializeToJSON.serialize,
        "xml": SerializeToXML.serialize,
    },
}
