import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print_book_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_book_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])




class Serialize:
    @staticmethod
    def serialize_json (book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def serialize_xml (book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")

class Commands:
    def __init__(self, book: Book):
        self.book = book

    def action(self, cmd: str) -> str | None:
        if cmd == "display console":
            self.book.display_console()
        elif cmd == "display reverse":
            self.book.display_reverse()
        elif cmd == "print book console":
            self.book.print_book_console()
        elif cmd == "print book reverse":
            self.book.print_book_reverse()
        elif cmd == "serialize json":
            return Serialize.serialize_json(self.book)
        elif cmd == "serialize xml":
            return Serialize.serialize_xml(self.book)
        else:
            print(f"Unknown command: {cmd}")
            return None


def main(book: Book, commands: list[str]) -> list[None | str]:
    command = Commands(book)
    result = []
    for cmd in commands:
        result.append(command.action(cmd))
    return result



if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    results = main(sample_book, ["display console", "serialize xml",])
    for result in results:
        print(result)
