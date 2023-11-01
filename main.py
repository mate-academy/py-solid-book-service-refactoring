from app.books import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, actions: list) -> None or str:

    actions_dict = {
        "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
        "print": {
            "console": (book.title, book.content),
            "reverse": (book.title, book.content[::-1])
        },
        "serialize": {"json": JSONSerializer, "xml": XMLSerializer},
    }

    for action, method in actions:
        if action == "display":
            actions_dict[action][method]().display(book)
        if action == "print":
            print(actions_dict[action][method])
        if action == "serialize":
            return actions_dict[action][method]().serialize(book)


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    actions = [
        ("display", "console"),
        ("display", "reverse"),
        ("print", "console"),
        ("print", "reverse"),
        ("serialize", "json"),
        ("serialize", "xml"),
    ]
    main(book, actions)
