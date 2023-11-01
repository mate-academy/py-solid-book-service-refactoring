from app.book import Book
from app.book_print import PrintBook
from app.book_serializer import SerializerFormat


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            PrintBook(book).print(method_type)
        elif cmd == "serialize":
            serializer = SerializerFormat.create_serializer(method_type, book)
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
