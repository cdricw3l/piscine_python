#! /usr/bin/python3

class SecurePlant:

    _name: str
    _height: int
    _age: int

    def __init__(self, name: str, height: int, age: int) -> None:

        if(height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return
        if (age < 0):
            print(f"Invalid operation attempted: height {age} days [REJECTED]")
            return

        self._name = name
        print("=== Garden Security System ===")
        print(f"Plant created: {self._name}")
        self._height = self.set_age(height)
        self._age = self.set_age(age)
   
    def set_height(self, height: int) -> None:
        if(height >= 0):
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    
    def set_age(self, height: int) -> None:
        if(height >= 0):
            self._height = height
            print(f"Age updated: {height} days [OK]")
        else:
            print(f"Invalid operation attempted: age {height} days [REJECTED]")
            print("Security: Negative age rejected")
    
    def get_height(self) -> int:
        return self._height
    
    def get_age(self) -> int:
        return self._age

    def get_info(self):
        print(f"Current plant: {self._name} ({self.get_height()}cm, {self.get_age()} days)")

if __name__ == "__main__":
    p1 = SecurePlant("rose", -10, 5)
    print("")
    print(p1 == None)
    p1.set_age(-10)
    p1.set_height(-10)
    print("")
    p1.get_info()
