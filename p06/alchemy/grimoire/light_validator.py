from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    valide: bool = False
    string: str = ""
    arr_str: list[str] = ingredients.split(' ') 
    size: int = len(arr_str) - 1
    for ingredient in arr_str:
        allowed: list[str] = [x.capitalize() for x in light_spell_allowed_ingredients()]
        if ingredient.capitalize() in allowed:
            valide = True
        string = string + f"{ingredient}, " #if arr_str.index(ingredient) < size - 2  else  string = string + f"{ingredient} and " if arr_str.index(ingredient) == size - 1 else string = string + f"{ingredient} "
    print(string)