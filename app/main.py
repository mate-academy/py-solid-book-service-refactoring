from app.models import Book
from app.display import DisplayFactory
from app.print import PrintFactory
from app.serializers import SerializerFactory


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = DisplayFactory.get_display_strategy(method_type)
            display_strategy.display(book.content)
        elif cmd == "print":
            print_strategy = PrintFactory.get_print_strategy(method_type)
            print_strategy.print_book(book.title, book.content)
        elif cmd == "serialize":
            serializer = SerializerFactory.get_serializer(method_type)
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book(
        title="Sample Book", content="This is some sample content."
    )
    sample_book.save()
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
