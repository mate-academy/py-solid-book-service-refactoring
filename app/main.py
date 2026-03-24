from app.handlers import CommandHandler
from app.models import Book
from app.displayers import DisplayService, PrintService
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {"json": JsonSerializer(), "xml": XmlSerializer()}
    handler = CommandHandler(DisplayService(), PrintService(), serializers)
    return handler.handle(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
