import json
from xml.etree import ElementTree

import pytest

from app.display import BookDisplay
from app.main import Book, main
from app.printer import BookPrinter
from app.serializer import BookSerializer
from app.service import BookService


@pytest.mark.parametrize(
    "command, method_type, expected",
    [
        ("display", "console", "abc\n"),
        ("display", "reverse", "cba\n"),
        ("print", "console", "Printing the book: Title...\nabc\n"),
        ("print", "reverse", "Printing the book in reverse: Title...\ncba\n"),
    ],
)
def test_exact_output(command, method_type, expected, capsys) -> None:
    assert main(Book("Title", "abc"), [(command, method_type)]) is None
    assert capsys.readouterr().out == expected


@pytest.mark.parametrize("command", ["display", "print", "serialize"])
def test_unknown_format(command) -> None:
    with pytest.raises(ValueError) as error:
        main(Book("Title", "abc"), [(command, "unknown")])
    assert str(error.value) == f"Unknown {command} type: unknown"


def test_serialization_stops_processing_commands(capsys) -> None:
    book = Book("Title", "abc")
    result = main(
        book,
        [("display", "console"), ("serialize", "json"), ("print", "reverse")],
    )
    assert result == '{"title": "Title", "content": "abc"}'
    assert capsys.readouterr().out == "abc\n"


@pytest.mark.parametrize("commands", [[], [("unknown", "console")]])
def test_commands_without_operations(commands, capsys) -> None:
    assert main(Book("Title", "abc"), commands) is None
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize("content", ["", 'Привет <book> & "quotes"'])
def test_serialization_preserves_content(content) -> None:
    book = Book(content, content)
    assert json.loads(main(book, [("serialize", "json")])) == {
        "title": content,
        "content": content,
    }
    root = ElementTree.fromstring(main(book, [("serialize", "xml")]))
    assert root.tag == "book"
    assert (root.find("title").text or "") == content
    assert (root.find("content").text or "") == content


def test_custom_implementations_can_be_injected(capsys) -> None:
    class TitleDisplay(BookDisplay):
        def display(self, book: Book) -> None:
            print(book.title)

    class TitlePrinter(BookPrinter):
        def print_book(self, book: Book) -> None:
            print(f"Title: {book.title}")

    class TitleSerializer(BookSerializer):
        def serialize(self, book: Book) -> str:
            return book.title

    service = BookService(
        displays={"title": TitleDisplay()},
        printers={"title": TitlePrinter()},
        serializers={"title": TitleSerializer()},
    )
    result = main(
        Book("Custom", "abc"),
        [("display", "title"), ("print", "title"), ("serialize", "title")],
        service=service,
    )
    assert result == "Custom"
    assert capsys.readouterr().out == "Custom\nTitle: Custom\n"
