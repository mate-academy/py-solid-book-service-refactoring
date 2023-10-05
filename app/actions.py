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


def get_acceptable_methods() -> set:
    methods = set()
    for action_methods in ACTIONS.values():
        for method in action_methods:
            methods.add(method)
    return methods


ACCEPTABLE_METHODS = get_acceptable_methods()
