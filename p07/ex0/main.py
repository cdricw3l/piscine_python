from abc import ABC, abstractmethod

class Creature(ABC):
    ___creature_name: str
    __creature_type: str

    def __init__(self, creature_name: str, creature_type: str):
        self.___creature_name = creature_name
        self.__creature_type = creature_type

    def get_name(self) -> str:
        return self.___creature_name
    
    def get_type(self) -> str:
        return self.__creature_type

    @abstractmethod
    def attack(self, attack: str) -> str:
        pass

class Flameling(Creature):

    def __init__(self, creature_name: str, creature_type: str):
        super().__init__(creature_name, creature_type)
    
    def attack(self, attack: str) -> str:
        return f"{self.___creature_name} use {attack}"