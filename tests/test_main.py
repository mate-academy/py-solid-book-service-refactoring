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
def test_data() -> tuple:
    return ("Sample Book", "This is some sample content.")


def test_display_console(test_data) -> None:
    output = get_stdout(main, *test_data, [("display", "console")])
    assert "This is some sample content." in output


def test_display_reverse(test_data) -> None:
    output = get_stdout(main, *test_data, [("display", "reverse")])
    assert "tnetnoc elpmas emos si sihT" in output


def test_print_console(test_data) -> None:
    output = get_stdout(main, *test_data, [("print", "console")])
    assert test_data[0] in output
    assert "This is some sample content." in output


def test_print_reverse(test_data) -> None:
    output = get_stdout(main, *test_data, [("print", "reverse")])
    assert test_data[0] in output
    assert "tnetnoc elpmas emos si sihT" in output


def test_serialize_json(test_data) -> None:
    serialized_book = main(*test_data, [("serialize", "json")])
    assert (
        serialized_book
        == '{"title": "Sample Book", "content": "This is some sample content."}'
    )


def test_serialize_xml(test_data) -> None:
    serialized_book = main(*test_data, [("serialize", "xml")])
    assert "<title>Sample Book</title>" in serialized_book
    assert "<content>This is some sample content.</content>" in serialized_book
