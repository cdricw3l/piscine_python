
from .elements import create_air, create_earth
from elements import create_fire, create_water
# Need to know why elements import element from the top of the project


def healing_potion() -> str:
    return f"Healing potion brewed with'{
        create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{
       create_fire()}' and '{create_water()}'"
