from app.book_display import DisplayConsole, DisplayReverse
from app.book_print import PrintConsole, PrintReverse
from app.book_serialize import SerializerJSON, SerializerXML


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_class = {
                "console": DisplayConsole,
                "reverse": DisplayReverse
            }
            display_class = display_class[method_type]
            display_object = display_class(title=book.title, content=book.content)
            display_object.display()
        elif cmd == "print":
            print_class = {
                "console": PrintConsole,
                "reverse": PrintReverse
            }
            print_class = print_class[method_type]
            print_object = print_class(title=book.title, content=book.content)
            print_object.print()
        elif cmd == "serialize":
            serializer_class = {
                "json": SerializerJSON,
                "xml": SerializerXML
            }
            serializer_class = serializer_class[method_type]
            serializer_object = serializer_class(title=book.title, content=book.content)
            return serializer_object.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
