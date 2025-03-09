from dataclasses import dataclass

from app.protocols import HasTitleAndContent


@dataclass
class Book(HasTitleAndContent):
    title: str
    content: str
