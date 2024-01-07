from app.book import Book
from app.command import SerializeCommand
from app.translator import CommandTranslator, DisplayerTranslator


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_translator = CommandTranslator()
    displayer_translator = DisplayerTranslator()

    for command, displayer_method in commands:
        command = command_translator.translate(command)
        displayer_method = displayer_translator.translate(displayer_method)
        result = command(displayer_method=displayer_method, book=book)
        if command is SerializeCommand.command:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
