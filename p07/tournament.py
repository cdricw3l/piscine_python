from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex2.strategy import BattleStrategy , NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponant: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(list)} opponents involved")



if __name__ == "__main__":
    
    flame_factory: FlameFactory =  FlameFactory()
    aqua_factory: AquaFactory =  AquaFactory()
    heal_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()



    # agressive: AggressiveStrategy = AggressiveStrategy()
    # defensive: DefensiveStrategy = DefensiveStrategy()
    normal: NormalStrategy = NormalStrategy(flame_factory.create_base())
    normal2: NormalStrategy = NormalStrategy(flame_factory.create_evolved())

    if normal.is_valide(flame_factory.create_base()):
        print("valide input")
    normal.act()
   