from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print import PrintConsole, PrintReverse
from app.serialize import SerializeJson, SerializeXml

data = {
    "display": {
        "console": DisplayConsole,
        "reverse": DisplayReverse,
    },
    "print": {
        "console": PrintConsole,
        "reverse": PrintReverse,
    },
    "serialize": {
        "json": SerializeJson,
        "xml": SerializeXml,
    }

}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd not in data:
            continue
        if method_type not in data[cmd]:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        result = data[cmd][method_type]().action(book)

        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "console"), ("serialize", "xml")]))
