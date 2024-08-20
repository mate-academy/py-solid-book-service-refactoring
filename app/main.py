from app.book import Book
from app.convert import ConvertJSON, ConvertXML
from app.display import DisplayConsole, DisplayReverse
from app.print import ConsolePrint, ReversePrint


manage = {
    "display": {"console": DisplayConsole,
                "reverse": DisplayReverse, },
    "print": {"console": ConsolePrint,
              "reverse": ReversePrint, },
    "serialize": {"json": ConvertJSON,
                  "xml": ConvertXML, }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        action = manage.get(cmd, {}).get(method_type)
        if action:
            result = action()(book.title, book.content)
            if result:
                return result
        else:
            raise ValueError(f"Unknown {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
