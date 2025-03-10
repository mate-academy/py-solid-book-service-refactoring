from typing import Dict, Callable


class DisplayMixin:
    def __init__(self) -> None:
        self._display_methods: Dict[str, Callable[[], None]] = {
            "console": self._display_console,
            "reverse": self._display_reverse
        }

    def _display_console(self) -> None:
        print(self.content)

    def _display_reverse(self) -> None:
        print(self.content[::-1])

    def display(self, display_type: str) -> None:
        method = self._display_methods.get(display_type)
        if method:
            method()
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class ExtendedDisplayMixin(DisplayMixin):
    def __init__(self) -> None:
        super().__init__()
        self._display_methods["uppercase"] = self._display_uppercase

    def _display_uppercase(self) -> None:
        print(self.content.upper())
