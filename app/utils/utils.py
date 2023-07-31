from app.utils.handlers import Display, Print, Serialize


def get_handler_by_type(
        method_type: str,
        handler_map: dict[str, Display | Print | Serialize]
) -> Display | Print | Serialize:
    if method_type in handler_map:
        handler_instance = handler_map[method_type]
        return handler_instance
    else:
        raise ValueError(f"Unknown type: {method_type}")
