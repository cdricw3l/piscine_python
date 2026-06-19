import sys


class Invalide_param(Exception):
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)

class Quantity_error(ValueError):
    def __init__(self, msg: str) -> None:
        ValueError.__init__(self, msg)

def get_key_value(arg:str) -> dict[str, int]:
    # try:
    #     kv: dict[str, int] = {}
    #     split: list[str] = arg.split(':')
    #     key: str = split[0]
    #     value: str = split[1]
    #     kv.update({key:value})
    # except (IndexError, ValueError) as e:
    #     if e.__class__.__name__ == IndexError.__name__:
    #         raise  Invalide_param(f"Error - invalid parameter '{}'")
    #     elif e.__class__.__name__ == ValueError.__name__:
    #         raise ValueError
def parsing_arg(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        split: list[str] = arg.split()
        
        key: str = split[0]
        value: str = split[1]


def test():
    try:
        int("abc")
    except ValueError:
        raise Quantity_error(f"Quantity error for 'abc'")

if __name__ == "__main__":
#    args: list[str] = sys.argv[1:]
#    parsing_arg(args)
    try:
        test()
    except Quantity_error as e:
        print(e)