from app.display_content import DisplayInConsole, DisplayToReversed
from app.models import Book
from app.print_book import PrintInConsole, PrintToReversed
from app.serializers import BookJsonSerializer, BookXmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    actions = {
        "display": {
            "console": DisplayInConsole.display_content,
            "reverse": DisplayToReversed.display_content,
        },
        "print": {
            "console": PrintInConsole.print_book,
            "reverse": PrintToReversed.print_book,
        },
        "serialize": {
            "json": BookJsonSerializer.serialize_book,
            "xml": BookXmlSerializer.serialize_book,
        },
    }

    for cmd, method_type in commands:
        if (cmd in actions) and (method_type in actions[cmd]):
            result = actions[cmd][method_type](book)

            if result:
                return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
