from io import StringIO
import sys

import pytest

from app.main import main, Book


def get_stdout(func, *args, **kwargs) -> str:
    new_stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = new_stdout

    func(*args, **kwargs)

    sys.stdout = old_stdout
    return new_stdout.getvalue()


@pytest.fixture()
def book() -> Book:
    return Book("Sample Book", "This is some sample content.")


def test_display_console(book) -> None:
    output = get_stdout(main, book, [("display", "console")])
    assert "This is some sample content." in output


def test_display_reverse(book) -> None:
    output = get_stdout(main, book, [("display", "reverse")])
    assert "tnetnoc elpmas emos si sihT" in output


def test_print_console(book) -> None:
    output = get_stdout(main, book, [("print", "console")])
    assert book.title in output
    assert "This is some sample content." in output


def test_print_reverse(book) -> None:
    output = get_stdout(main, book, [("print", "reverse")])
    assert book.title in output
    assert "tnetnoc elpmas emos si sihT" in output


def test_serialize_json(book) -> None:
    serialized_book = main(book, [("serialize", "json")])
    assert (
        serialized_book
        == '{"title": "Sample Book", "content": "This is some sample content."}'
    )


def test_serialize_xml(book) -> None:
    serialized_book = main(book, [("serialize", "xml")])
    assert "<title>Sample Book</title>" in serialized_book
    assert "<content>This is some sample content.</content>" in serialized_book
