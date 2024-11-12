from app.models import Book
from app.serializers import (
    GetTypeConvertOrException,
    GetTypePrintOrException,
    GetTypeDisplayOrException
)


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    results = []

    commands_dict = {
        "serialize": GetTypeConvertOrException,
        "print": GetTypePrintOrException,
        "display": GetTypeDisplayOrException
    }

    for cmd, method_type in commands:
        if cmd == "serialize":
            result = commands_dict[cmd](data=book, action_type=method_type)
            results.append(result.command())
        if cmd == "display":
            result = commands_dict[cmd](
                data=book.content,
                action_type=method_type
            )
            results.append(result.command())
        if cmd == "print":
            result = commands_dict[cmd](
                obj_title=book.title,
                data=book.content,
                action_type=method_type
            )
            results.append(result.command())

    final_result = "\n".join(filter(None, results))
    print(final_result)
    return final_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(sample_book, [("display", "console")])
