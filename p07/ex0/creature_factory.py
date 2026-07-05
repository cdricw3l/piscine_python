from abc import ABC, abstractmethod


class Creature(ABC):
    __name: str
    __type: str

    def __init__(self, name: str, type: str) -> None:
        self.__name = name.capitalize()
        self.__type = type.capitalize()

    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.__name} is a {self.__type} Creature"


class Flameling(Creature):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Flameling', 'Fire')
        self.__attack = 'Ember'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"


class Pyrodon(Creature):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Pyrodon', ' Fire/Flying')
        self.__attack = 'Flamethrower'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"


class Aquabub(Creature):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Aquabub', 'Water')
        self.__attack = 'Water Gun'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"


class Torragon(Creature):

    __attack: str

    def __init__(self) -> None:
        super().__init__('Torragon', 'Water')
        self.__attack = 'Hydro Pump'

    def attack(self) -> str:
        return f"{self.get_name()} use {self.__attack}!"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
