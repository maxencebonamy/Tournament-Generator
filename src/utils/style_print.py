from typing import List


class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    _ENDC = '\033[0m'

def style_print(text: str, *args: List[Style]) -> None:
    print(f"{''.join(args)}{text}{Style._ENDC}")

def style_input(*args: List[Style]) -> str:
    print(''.join(args), end="")
    output = input()
    print(Style._ENDC, end="")
    return output