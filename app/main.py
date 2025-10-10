from models import ConsoleBook, ReverseBook
from serializers import Json, Xml


def main(title: str,
         content: str,
         commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if method_type == "console":
            book = ConsoleBook(title, content)
        else:
            book = ReverseBook(title, content)
        if cmd == "display":
            book.display()
        elif cmd == "print":
            book.print_book()
        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(Json(title, content))
            elif method_type == "xml":
                return book.serialize(Xml(title, content))


if __name__ == "__main__":
    title = "Sample Book"
    content = "This is some sample content."
    print(main(title, content, [("display", "reverse"), ("serialize", "xml")]))
