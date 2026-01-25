from app.enums import DisplayType
from app.interfaces import HasContent
from app.display import ConsoleDisplay, ReverseDisplay


class DisplayService:
    def display(self, book: HasContent, display_type: str) -> None:
        dt = DisplayType.from_str(display_type)
        match dt:
            case DisplayType.CONSOLE:
                ConsoleDisplay().display(book)
            case DisplayType.REVERSE:
                ReverseDisplay().display(book)
