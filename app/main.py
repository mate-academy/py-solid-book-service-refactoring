from app.book import Book
from app.convert import ConvertJson, ConvertXml
from app.display import DisplayConsole, DisplayReverse
from app.print import PrintConsole, PrintReverse


manage = {
    "display": {"console": DisplayConsole,
                "reverse": DisplayReverse, },
    "print": {"console": PrintConsole,
              "reverse": PrintReverse, },
    "serialize": {"json": ConvertJson,
                  "xml": ConvertXml, }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if (action := manage.get(cmd, {}).get(method_type)):
            if (res := action()(book.title, book.content)):
                return res

        else:
            raise ValueError(f"Unknown {cmd} type2: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
