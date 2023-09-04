from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.print import ConsolePrintBook, ReversePrintBook
from app.serializer import JSONSerializeBook, XMLSerializeBook

DISPLAY_COMMANDS = {
    "console": ConsoleDisplayBook,
    "reverse": ReverseDisplayBook
}

PRINT_COMMANDS = {
    "console": ConsolePrintBook,
    "reverse": ReversePrintBook
}

SERIALIZE_COMMANDS = {
    "json": JSONSerializeBook,
    "xml": XMLSerializeBook
}
