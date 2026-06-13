#! /usr/bin/python3

class Plant:
    """ Plant class that serves as a blueprint for any plan """
    name: str
    height: int
    age: int

    def __init__(self, name, height, age):
        """
        The constructor that initializes instances
        with attributes for name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    p1 = Plant("rose", 1, 10)
    p2 = Plant("cana", 10, 110)
    p3 = Plant("bego", 9, 21)

    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
