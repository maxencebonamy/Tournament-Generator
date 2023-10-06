from typing import Callable


def condition_input(text: str, condition: Callable[[str], bool], onError: Callable[[], None] = lambda: None) -> str:
    value: str = None
    while True:
        value = input(text)
        if condition(value):
            break
        onError()
    return value