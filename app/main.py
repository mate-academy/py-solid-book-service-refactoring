from app.displays import DisplayCMD
from app.prints import PrintCMD
from app.serializers import SerializeCMD


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.__title = title
        self.__content = content

    @property
    def title(self) -> str:
        return self.__title

    @property
    def content(self) -> str:
        return self.__content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayCMD.display(method_type, book)
        elif cmd == "print":
            PrintCMD.print_object(method_type, book)
        elif cmd == "serialize":
            return SerializeCMD.serialize(method_type, book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("print", "no_space"),
                ("serialize", "xml")
            ]
        )
    )
