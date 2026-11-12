from app.operations import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolPrint,
    ReversePrint,
    XmlSerializer,
    JsonSerializer,
    Book,
)

from app.services import GetOutputService

dict_operations = {
    ("display", "console"): ConsoleDisplay(),
    ("display", "reverse"): ReverseDisplay(),
    ("print", "console"): ConsolPrint(),
    ("print", "reverse"): ReversePrint(),
    ("serialize", "xml"): XmlSerializer(),
    ("serialize", "json"): JsonSerializer()
}


def main(book: Book, operations: list[tuple[str, str]]) -> str:
    factory = GetOutputService(dict_operations)

    for operation in operations:
        service = factory.get_operation(operation)
        service_output = service.output(book)

    return service_output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
