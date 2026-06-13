#! /usr/bin/python3

class Plant:

    counter = 0
    """ 
    Plant class that serves as a blueprint for any plant
    and track the number of plan created
    """
    def __init__(self, name: str, height: int, age: int):
        """
        The constructor that initializes instances
        with attributes for name, height, and age,
        and display a creation message
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.counter += 1
        print(f"Created: {name} ({height}cm, {age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("rose", 0, 1)
    p2 = Plant("tullipe", 0, 1)
    p3 = Plant("begonia", 0, 1)
    p4 = Plant("maculata", 0, 1)
    p5 = Plant("margueritte", 0, 1)
    print(f"\nTotal plants created: {Plant.counter}")
    