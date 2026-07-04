from ..grimoire import validate_ingredients

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    ingrdients_check: str = validate_ingredients(ingredients)
    print(f"Spell recorded: {spell_name} {ingrdients_check}")