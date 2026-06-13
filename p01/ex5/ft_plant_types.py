#! /usr/bin/python3

class Plan:
    name:str
    height:int
    age: int
    type: str
    def __init__(self, type:str, name:str, height:int, age:int):
        if(height < 0):
            return None
        if(age < 0):
            return None
        self._name = name.capitalize()
        self._age = age
        self._height = height
        self.type = type.capitalize()

    def get_info(self) -> str:
        return f"{self._name} ({self.type}): {self._height}cm, {self._age} days"

class Flower(Plan):
    
    color:str

    def __init__(self, name:str, height:int, age:int, color:str):
        r = super().__init__("Flower", name, height, age)
        if(r == None):
            return
        self.color = color

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")

    def __str__(self) -> str:
        return f"{self.get_info()}, {self.color} color"


class Tree(Plan):

    trunk_diameter: int

    def __init__(self, name:str, height:int, age:int, trunk_diameter:int):
        r = super().__init__("Tree", name, height, age)
        if(r == None):
            return
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade: int) -> None:
        print(f"{self._name} provides {shade} square meters of shade")

    def __str__(self) -> str:
        return f"{self.get_info()}, {self.trunk_diameter} diameter"

class Vegetable(Plan):

    harvest_season: str
    nutritional_value: str

    def __init__(self, name:str, height:int, age:int, harvest_season: str,nutritional_value: str):
        r = super().__init__("Vegetable", name, height, age)
        if(r == None):
            return
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> str:
        return f"{self.get_info()}, {self.harvest_season} harvest"



if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    f1 = Flower("rose", 35, 10, "red")
    print(f1)
    f1.bloom()

    f2 = Tree("chene", 30, 10, 25)
    print(f2)
    f2.produce_shade(32)

    f3 = Vegetable("tomato", -55,20,"summer", "rich in vitamine c")
    print(f3 == None)
