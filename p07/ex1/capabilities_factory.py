from abc import ABC, abstractmethod
from ex0.creature_factory import CreatureFactory, Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    __attack: str

    def __init__(self) -> None:
        self.__attack = 'attacks normally'

    def set_attack(self, attack: str) -> None:
        self.__attack = attack

    def get_attack(self) -> str:
        return f"{self.__attack}"

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Sproutling', 'Grass')
        self.__attack = 'Vine Whip'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"

    def heal(self) -> str:
        return f"{self.get_name()} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Bloomelle', 'Grass/Fairy')
        self.__attack = 'Petal Dance'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"

    def heal(self) -> str:
        return f"{self.get_name()} heals itself and others for a small amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, 'Shiftling', 'Normal')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.get_name()} {self.get_attack()}!"

    def transform(self) -> str:
        self.set_attack("unleashes a devastating morph strike")
        return f"{self.get_name()} shifts into a sharper form!"

    def revert(self) -> str:
        self.set_attack("attacks normally")
        return f"{self.get_name()} returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, 'Shiftling', 'Normal')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.get_name()} {self.get_attack()}!"

    def transform(self) -> str:
        self.set_attack("unleashes a devastating morph strike")
        return f"{self.get_name()} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.set_attack("attacks normally")
        return f"{self.get_name()} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
