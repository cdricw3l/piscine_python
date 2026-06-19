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
            if split[0] not in inventory:
                inventory.update(kv)
            else:
                print(f"Redundant item '{split[0]}'- discarding")
        except Invalide_param as e:
            print(e)
        except ValueError as e:
            print(e)
    return inventory



if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    d: dict[str, int] = parsing_arg(args)
    print(f"Got inventory: {d}")
