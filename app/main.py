from models.book import Book
from services.book_service import BookService

def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    for cmd, method_type in commands:
        if cmd == "display":
            service.display(method_type)
        elif cmd == "print":
            service.print_book(method_type)
        elif cmd == "serialize":
            return service.serialize(method_type)

if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))