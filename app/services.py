from app.books import Book
from app.displayers import BookDisplayer
from app.printers import BookPrinter
from app.serializers import BookSerializer


class BookService:
    def __init__(
            self,
            displayer: BookDisplayer,
            printer: BookPrinter,
            serializer: BookSerializer,
    ) -> None:
        self.displayer = displayer
        self.printer = printer
        self.serializer = serializer

    def display(self, book: Book) -> None:
        self.displayer.display(book)

    def print_book(self, book: Book) -> None:
        self.printer.print_book(book)

    def serialize(self, book: Book) -> str:
        return self.serializer.serialize(book)
