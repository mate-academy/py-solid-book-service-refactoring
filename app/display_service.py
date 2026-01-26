from app.enums import DisplayType
from app.interfaces import HasContent
from app.display import DisplayStrategy


class DisplayService:
    def __init__(self, displays: dict[DisplayType, DisplayStrategy]) -> None:
        self.displays = displays

    def display(self, book: HasContent, display_type: str) -> None:
        dt = DisplayType.from_str(display_type)
        display_strategy = self.displays.get(dt)

        if display_strategy is None:
            raise ValueError(
                f"No display strategy found for type: {display_type}"
            )

        display_strategy.display(book)
