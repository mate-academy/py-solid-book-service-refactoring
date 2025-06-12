from app.serializers.book_serializer import BookSerializer
from app.book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "print":
            cmd = "print_book"
        if cmd == "serialize":
            serializer = BookSerializer(book)
            if not hasattr(serializer, method_type):
                raise ValueError(f"Unknown serialize type: {method_type}")
            return getattr(serializer, method_type)()
        elif hasattr(book, cmd):
            getattr(book, cmd)(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
