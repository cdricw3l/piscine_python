from typing import Callable, Any


class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    counter: int = initial_power

    def acc(add: int) -> int:
        nonlocal counter
        counter += add
        return counter
    return acc


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, (Callable[[Any, Any], None] | Callable[[Any], Any | str])]:
    vault: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        nonlocal vault
        vault.update({key: value})

    def recall(key: Any) -> Any | str:
        value: Any = vault.get(key)
        if value is None:
            return "Memory not found"
        return value
    return {'store': store, 'recall': recall}


def mage_counter_test() -> None:
    counter_a: Callable[[], int] = mage_counter()
    counter_b: Callable[[], int] = mage_counter()
    print(f"{Color.YELLOW}Testing mage counter...{Color.RESET}")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"counter_b call 2: {counter_b()}")
    print(f"counter_a call 4: {counter_a()}")
    print(f"counter_a call 5: {counter_b()}")


def spell_accumulator_test(base: int, add: list[int]) -> None:

    try:
        print(f"\n{Color.YELLOW}Testing spell accumulator...{Color.RESET}")
        acc: Callable[[int], int] = spell_accumulator(100)
        for value in add:
            print(f"Base {base}, add {value}: {acc(value)}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def enchantment_factory_test(enchantment_types: list[str],
                             items_to_enchant: list[str]) -> None:

    print(f"\n{Color.YELLOW}Testing enchantment factory...{Color.RESET}")
    try:
        for enchantment in enchantment_types:
            for item in items_to_enchant:
                factory: Callable[[str], str] = enchantment_factory(enchantment)
                print(factory(item))
            print()
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


def memory_vault_test() -> None:
    print(f"\n{Color.YELLOW}Testing memory vault...{Color.RESET}")
    vault: dict[str, Callable[[Any, Any], None] | Callable[[Any], Any | str]] = memory_vault()
    print("Store 'secret'= 42")
    store: Callable[[Any, Any], None]  = vault['store']
    call: Callable[[Any], Any | str] = vault['recall']
    store('secret', 42)
    print(f"Recall 'secret': {call('secret')}")
    print(f"Recall 'unknown': {call('unknown')}")


if __name__ == "__main__":
    initial_powers = [51, 28, 55]
    power_additions = [18, 12, 12, 8, 18]
    enchantment_types = ['Shocking', 'Windy', 'Flowing']
    items_to_enchant = ['Ring', 'Shield', 'Wand', 'Armor']

    mage_counter_test()
    spell_accumulator_test(100, [20, 30, 1])
    enchantment_factory_test(enchantment_types, items_to_enchant)
    memory_vault_test()
