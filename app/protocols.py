from typing import Protocol


class HasTitle(Protocol):
    title: str


class HasContent(Protocol):
    content: str


class HasTitleAndContent(HasTitle, HasContent, Protocol):
    pass
