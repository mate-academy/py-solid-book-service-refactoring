from app.book import Book
from app.display import Display
from app.print import Print
from app.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    valid_method_types = ["reverse", "console", "xml", "json"]
    instances = [Display(), Print(), Serializer()]

    for cmd, method_type in commands:
        if method_type not in valid_method_types:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        for instance in instances:
            if cmd == instance.cmd_type:
                result = getattr(instance, method_type)(book)

                if result is not None:
                    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
