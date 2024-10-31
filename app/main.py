from app.display_strategy import ConsoleDisplay, ReverseDisplay
from app.print_strategy import ReversePrint, ConsolePrint
from app.serialize_strategy import JsonSerializer, XmlSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    output = ""

    for action, action_type in commands:
        if action == "display":

            if action_type == "console":
                ConsoleDisplay().display(book.content)
            else:
                ReverseDisplay().display(book.content)

        elif action == "print":

            if action_type == "console":
                ConsolePrint().print_book(book. title, book.content)
            else:
                ReversePrint().print_book(book.title, book.content)

        elif action == "serialize":

            if action_type == "json":
                output = JsonSerializer().serialize(book. title, book.content)
            else:
                output = XmlSerializer().serialize(book.title, book.content)

    return output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
