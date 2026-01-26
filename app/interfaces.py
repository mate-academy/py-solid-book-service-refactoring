from __future__ import annotations

from typing import Protocol


class HasContent(Protocol):
    content: str


class HasTitleContent(Protocol):
    title: str
    content: str
