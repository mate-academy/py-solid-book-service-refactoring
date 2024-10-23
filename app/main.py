from app.utils import get_display_type, get_printer, get_serializer


class Entity:
    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = content

    def get_entity_name(self) -> str:
        return self.__class__.__name__.lower()


class Book(Entity):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        if command == "display":
            display = get_display_type(method_type)
            display.display(book.content)
        elif command == "print":
            printer = get_printer(method_type)
            printer.print_entity(
                book.get_entity_name(),
                book.title,
                book.content
            )
        elif command == "serialize":
            serializer = get_serializer(method_type)
            return serializer.serialize(
                book.get_entity_name(),
                book.title,
                book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
