from app.factory import ActionFactory
from app.models import Book


def main():
    sample_book = Book("Sample Book", "This is some sample content.")

    commands = [
        ("display", "reverse"),
        ("serialize", "xml"),
    ]
    for cmd, method_type in commands:
        try:
            action = ActionFactory.get_action(cmd, method_type)
            result = action.execute(sample_book)
            if result:
                print(f"Result: {result}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
