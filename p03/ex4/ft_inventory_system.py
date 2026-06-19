import sys


class Invalide_param(Exception):
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)

class Quantity_error(ValueError):
    def __init__(self) -> None:
        ValueError.__init__(self)

def get_key_value(split: list[str]) -> dict[str, int]:
    kv: dict[str, int] = {}
    try:
        key: str = split[0]
        value: str = int(split[1])
        kv.update({key:value})
    except IndexError:
        raise  Invalide_param(f"Error - invalid parameter '{key}'")
    except ValueError as e:
        raise ValueError(f"Quantity error for '{key}': {e}")
    return kv

def parsing_arg(args: list[str]) -> dict[str, int]:
    inventory: dict = {}
    for arg in args:
        try:
            split: list[str] = arg.split(':')
            kv: dict[str, int] = get_key_value(split)
            print(kv)
            inventory.update(kv)
        except Invalide_param as e:
            print(e)
        except ValueError as e:
            print(e)
    return inventory

def remove_dupplicate(args: list[str]) -> list[str]:
    unique_args: list[str] = []
    
# if __name__ == "__main__":
#     args: list[str] = sys.argv[1:]
#     unique_args: list[str] = []
#     [unique_args.append(arg) for arg in args if arg not in unique_args]
#     print(unique_args)
#     # d: dict[str, int] = parsing_arg(args)

if __name__ == "__main__":
    l: list[str] = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1", "sword:1", "hello", "key:value"]
    s: set[str] = set(l)
    print(s)