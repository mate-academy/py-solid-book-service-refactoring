from app.displayers import ConsoleBookDisplayer, ReverseBookDisplayer
from app.models import Book
from app.printers import ConsoleBookPrinter, ReverseBookPrinter
from app.serializers import JsonBookSerializer, XmlBookSerializer
from app.services import BookService


__all__ = ["Book", "main"]


DISPLAYERS = {
    "console": ConsoleBookDisplayer(),
    "reverse": ReverseBookDisplayer(),
}
PRINTERS = {
    "console": ConsoleBookPrinter(),
    "reverse": ReverseBookPrinter(),
}
SERIALIZERS = {
    "json": JsonBookSerializer(),
    "xml": XmlBookSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book, DISPLAYERS, PRINTERS, SERIALIZERS)
    return service.execute(commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
