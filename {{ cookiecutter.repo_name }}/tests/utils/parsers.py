def boolean_parser(string: str) -> bool:
    if string.lower() in ("true", "yes", "y", "1", "on"):
        return True

    if string.lower() in ("false", "no", "n", "0", "off"):
        return False

    msg = f"cannot convert '{string}' into boolean"
    raise ValueError(msg)
