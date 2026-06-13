#! /usr/bin/python3

class Plant:

    """ Plant class that serves as a blueprint for any plan """
    def __init__(self, name: str, height: int, age: int):
        """
        The constructor that initializes instances
        with attributes for name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """ increase the size of the plant """
        self.height += 1

    def age(self):
        """ increase the age of the plant """
        self.age += 1

    def get_info(self, day: int):
        """ display informations about the current plant status """
        print(f"=== Day {day} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("rose", 25, 30)
    i = 1
    p1.get_info(1)
    while (i < 7):
        p1.grow()
        p1.age()
        i += 1
    p1.get_info(i)
