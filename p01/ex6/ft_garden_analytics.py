#!/usr/bin/python3

class Plant:

    name:str
    height:int
    age:int

    def __init__(self, name:str, height:str, age:int):
        if(height < 0):
            return None
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self) -> str:
        return (f"- {self.name}: {self.height}cm")

class FloweringPlan(Plant):

    color = int

    def __init__(self, name:str, height:int, age:int, color:str):
        super().__init__(name, height, age)
        self.color = color
    
    def __str__(self):
        return (f"- {super.__str__}, {self.color} (blooming)")

class PrizeFlower(FloweringPlan):
    
    prize: int

    def __init__(self, name:str, height:int, age:int, color:str, prize:int):
        super().__init__(name, height, age, color)
        self.prize = prize
    
    def __str__(self):
        return (f"{super.__str__}, Prize points: {self.prize}")

class Network:

    owner : str
    plan : list[Plant]

    def __init__(self, owner: str):
        self.owner = owner
        self.plan = []

class GardenManager:

    network = list[Network]

    def __init__(self):
        self.network = []

    def create_garden_network(self, owner:str):
        net = Network(owner.capitalize())
        self.network.append(net)
        print(f"{net.owner} garden created")
    
    def list_network(self):
        n:  Network
        for n in self.network:
            p: Plant = n.plan
    
    def create_plant(self, owner:str, name:str, height:int, age:int):
        n:  Network
        for n in self.network:
            if(n.owner == owner.capitalize()):
                plan = Plant(name,height,age)
                print(f"Added {plan.name} to {n.owner} garden")
                n.plan.append(plan)




if __name__ == "__main__":
    garden = GardenManager()
    print("")
    garden.create_garden_network("Alice")
    print("")
    garden.create_plant("Alice", "Rose", 10, 0)
    garden.create_plant("Alice", "Oak Tree", 7, 0)
    garden.create_plant("Alice", "Sunflower", 2, 0)