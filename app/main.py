import json
import xml.etree.ElementTree as ElementTree


# --- Book ---
class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# --- Display Strategies ---
class DisplayStrategy:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


# --- Print Strategies ---
class PrintStrategy:
    def print(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


# --- Serialize Strategies ---
class SerializeStrategy:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")


# --- Main ---
def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        },
        "print": {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        },
        "serialize": {
            "json": JsonSerialize(),
            "xml": XmlSerialize(),
        },
    }

    result: str | None = None
    for cmd, method_type in commands:
        strategy = actions.get(cmd, {}).get(method_type)
        if not strategy:
            raise ValueError(f"Unknown command: {cmd} {method_type}")

        if cmd == "display":
            strategy.display(book)
        elif cmd == "print":
            strategy.print(book)
        elif cmd == "serialize":
            result = strategy.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
