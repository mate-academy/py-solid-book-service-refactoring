from app.interfaces import (
    BookDisplayInterface,
    BookPrintInterface,
    BookSerializeInterface,
    DisplayConsole,
    DisplayReverse,
    PrintReverse,
    PrintConsole,
    SerializeJson,
    SerializeXml
)


# Dictionaries mapping strategy names to their respective classes
DISPLAY_STRATEGIES: dict[str, type[BookDisplayInterface]] = {
    "console": DisplayConsole,
    "reverse": DisplayReverse
}

PRINT_STRATEGIES: dict[str, type[BookPrintInterface]] = {
    "console": PrintConsole,
    "reverse": PrintReverse
}

SERIALIZE_STRATEGIES: dict[str, type[BookSerializeInterface]] = {
    "json": SerializeJson,
    "xml": SerializeXml
}
