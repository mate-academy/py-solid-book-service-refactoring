from book import Book
from display import BookDisplay
from serialization import BookSerialization


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(book, method_type)
        elif cmd == "print":
            BookDisplay.print_book(book, method_type)
        elif cmd == "serialize":
            return BookSerialization.serialize(book, method_type)



if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))