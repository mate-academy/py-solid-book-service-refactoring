from app.models import Book
from app.services import BookCommand, create_default_book_processor


def main(book: Book, commands: list[BookCommand]) -> None | str:
    book_processor = create_default_book_processor()
    return book_processor.execute(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
