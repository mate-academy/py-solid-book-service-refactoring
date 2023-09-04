from app.book import Book, BookSerializer, BookFormatter


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        if cmd in ["display", "print"]:
            BookFormatter(book).formate(method_type, cmd)
        elif cmd == "serialize":
            return BookSerializer(book).serialize_from_commands(method_type)
