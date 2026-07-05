from abc import ABC, abstractmethod
from ex0.creature_factory import Creature
from ex1.capabilities_factory import TransformCreatureFactory, HealingCreatureFactory, CreatureFactory, TransformCapability
class BattleStrategy(ABC):

    @abstractmethod
    def act(self):
        pass
    
    @abstractmethod
    def is_valide(self) -> bool:
        pass

class NormalStrategy(BattleStrategy):
    
    __creature: Creature

    def __init__(self, creature: Creature):
        super().__init__()
        self.__creature = creature
    
    def is_valide(self, creature: Creature):
        if  issubclass(creature.__class__, Creature):
            return True
        return False
    
    def act(self):
        print(self.__creature.attack())

class AggressiveStrategy(BattleStrategy):

    __creature: TransformCapability
    
    def __init__(self, creature: TransformCapability):
        super().__init__()
        self.__creature = creature

    def is_valide(self, creature):
        if  issubclass(creature.__class__, TransformCreatureFactory):
            return True
        return False

    def act(self):
        print(self.__creature.transform())

class DefensiveStrategy(BattleStrategy):
    def is_valide(self, creature: Creature):
        if  issubclass(creature.__class__, HealingCreatureFactory):
            return True
        return False

    def act(self):
        pass
