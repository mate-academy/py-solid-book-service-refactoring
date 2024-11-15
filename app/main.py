from app.objects import Book
from app.output import DisplayBook, OutputObject, PrintBook
from app.serializers import BookJSONSerializer, BookXMLSerializer


def display(
        book: Book,
        output_class: OutputObject,
        method_type: str
) -> None:
    if method_type == "console":
        output_class.output_object(book)
    elif method_type == "reverse":
        output_class.output_object_reverse(book)


def print_book(
        book: Book,
        output_class: OutputObject,
        method_type: str
) -> None:
    if method_type == "console":
        output_class.output_object(book)
    elif method_type == "reverse":
        output_class.output_object_reverse(book)


def serialize(book: Book, method_type: str) -> str:

    serializer_classes = {
        "json": BookJSONSerializer,
        "xml": BookXMLSerializer,
    }

    serializer_class = serializer_classes[method_type]
    serializer = serializer_class(book)
    return serializer.serialize()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            output_class = DisplayBook()
            display(book, output_class, method_type)
        elif cmd == "print":
            output_class = PrintBook()
            print_book(book, output_class, method_type)
        elif cmd == "serialize":
            return serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
