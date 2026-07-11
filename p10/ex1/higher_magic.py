
from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def attack(target: str, power: int) -> str:
        return f"Attack {target} for {power} HP"


def strong_attack(target: str, power: int) -> str:
        return f"Strongest Attack {target} for {power * 10} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
            if condition(target, power):
                return spell(target, power)
            else:
                return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence
         

def condition_test(target: str, power: int) -> bool:
    if target == 'Dragon' and power > 10:
        return True
    else:
        return False

if __name__ == "__main__":
    test_values = [13, 13, 19]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined: Callable =  spell_combiner(attack, heal)
    comb: tuple = combined('Dragon', 10)
    print(comb[0], comb[1])

    amplifier: Callable = power_amplifier(attack , 10)
    print(amplifier('Dragon', 10))

    conditional: Callable = conditional_caster(condition_test, strong_attack)
    print(conditional('Dragon', 11))

    sequence: Callable = spell_sequence([attack, attack, heal])
    l = sequence('dragon', 10)
    
    