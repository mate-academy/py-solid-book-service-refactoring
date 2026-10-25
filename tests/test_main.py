"""Tests for the book service main module."""

from io import StringIO
import sys
from typing import Callable, Any

import pytest

from app.main import main
from app.domain.book import Book


def get_stdout(
    func: Callable[..., Any], *args: Any, **kwargs: Any
) -> str:
    new_stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = new_stdout

    func(*args, **kwargs)

    sys.stdout = old_stdout
    return new_stdout.getvalue()


@pytest.fixture()
def book() -> Book:
    return Book("Sample Book", "This is some sample content.")


def test_display_console(book: Book) -> None:
    output = get_stdout(main, book, [("display", "console")])
    assert "This is some sample content." in output


def test_display_reverse(book: Book) -> None:
    output = get_stdout(main, book, [("display", "reverse")])
    assert "tnetnoc elpmas emos si sihT" in output


def test_print_console(book: Book) -> None:
    output = get_stdout(main, book, [("print", "console")])
    assert book.title in output
    assert "This is some sample content." in output


def test_print_reverse(book: Book) -> None:
    output = get_stdout(main, book, [("print", "reverse")])
    assert book.title in output
    assert "tnetnoc elpmas emos si sihT" in output


def test_serialize_json(book: Book) -> None:
    serialized_book = main(book, [("serialize", "json")])
    expected = (
        '{"title": "Sample Book", "content": "This is some sample content."}'
    )
    assert serialized_book == expected


def test_serialize_xml(book: Book) -> None:
    serialized_book = main(book, [("serialize", "xml")])
    assert "<title>Sample Book</title>" in serialized_book
    assert "<content>This is some sample content.</content>" in serialized_book
