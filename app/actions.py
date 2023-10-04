from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializeJSON, SerializeXML

ACTIONS = {
    "display": {
        "console": DisplayConsole,
        "reverse": DisplayReverse,
    },
    "print": {
        "console": PrintConsole,
        "reverse": PrintReverse,
    },
    "serialize": {
        "json": SerializeJSON,
        "xml": SerializeXML,
    }
}


def get_acceptable_methods():
    methods = set()
    for value in ACTIONS.values():
        for key in value:
            methods.add(key)
    return methods


ACCEPTABLE_METHODS = get_acceptable_methods()
