from abc import ABC, abstractmethod

class Creature(ABC):
    ___creature_name: str
    __creature_type: str

    def __init__(self, creature_name: str, creature_type: str):
        self.___creature_name = creature_name.capitalize()
        self.__creature_type = creature_type.capitalize()

    def get_name(self) -> str:
        return self.___creature_name
    
    def get_type(self) -> str:
        return self.__creature_type

    @abstractmethod
    def attack(self, attack: str) -> str:
        pass

    def describe(self) -> str:
        return f"{self.___creature_name} is a {self.__creature_type} type Creature"

class Flameling(Creature):

    def __init__(self, creature_name: str, creature_type: str = 'Fire'):
        super().__init__(creature_name, creature_type)
    
    def attack(self, attack: str) -> str:
        return f"{self.___creature_name} use {attack}"

class Pyrodon(Creature):

    def __init__(self, creature_name: str, creature_type: str = ' Fire/Flying'):
        super().__init__(creature_name, creature_type)
    
    def attack(self, attack: str) -> str:
        return f"{self.___creature_name} use {attack}"

class Aquabub(Creature):

    def __init__(self, creature_name: str, creature_type: str = 'Water'):
        super().__init__(creature_name, creature_type)
    
    def attack(self, attack: str) -> str:
        return f"{self.___creature_name} use {attack}"

class Torragon(Creature):

    def __init__(self, creature_name: str, creature_type: str = 'Water'):
        super().__init__(creature_name, creature_type)
    
    def attack(self, attack: str) -> str:
        return f"{self.___creature_name} use {attack}"