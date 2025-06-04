import json


def to_json(title: str, content: str) -> str:
    return json.dumps({"title": title, "content": content})
