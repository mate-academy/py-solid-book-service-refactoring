from service.display import DisplayOut, DisplayReverse
from service.handler import DisplayOutput, PrintOutput
from service.serialize import JsonSerializeOutput, XmlSerializeOutput


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                show_display = DisplayOut()
            elif method_type == "reverse":
                show_display = DisplayReverse()
            else:
                raise ValueError(f"Unknown display method: {method_type}")
            show_display.display(book.content)

        elif cmd == "print":
            if method_type == "console":
                show_print = DisplayOutput()
            elif method_type == "reverse":
                show_print = PrintOutput()
            else:
                raise ValueError(f"Unknown print method: {method_type}")
            show_print.output(book.title, book.content)

        elif cmd == "serialize":
            if method_type == "json":
                show_serialize = JsonSerializeOutput()
            elif method_type == "xml":
                show_serialize = XmlSerializeOutput()
            else:
                raise ValueError(f"Unknown serialization method: "
                                 f"{method_type}")
            return show_serialize.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
