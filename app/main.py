from app.book.factories.action_factory import BookActionFactory
from app.book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    data_list = []
    for action_type, method_type in commands:
        action_factory = BookActionFactory.get_action_factory(action_type)
        method = action_factory.get_book_method(method_type)
        data = method.method(book)
        if data:
            data_list.append(data)
    if len(data_list):
        return "\n".join(data_list)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    command_list = [
        ("display", "console"),
        ("display", "reverse"),
        ("print", "console"),
        ("print", "reverse"),
        ("serialize", "xml"),
        ("serialize", "json"),
        ("display", "wrong method"),
    ]
    print(main(sample_book, command_list))
