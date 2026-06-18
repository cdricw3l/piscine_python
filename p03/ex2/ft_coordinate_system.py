import math

class invalid_syntax(Exception):
    def __init__(self, msg: str = "Invalid syntax") -> None:
        Exception.__init__(self, msg)
    def __str__(self):
        return Exception.__dict__
class Distance_data():
    x: tuple[float]
    y: tuple[float]
    z: tuple[float]

    def __init__(self, t1: tuple[float], t2: tuple[float]) -> None:
        self.x1 = t1[0]
        self.y1 = t2[1]
        self.z1 = t3[2]
        self.x2 = data[3]
        self.y2 = data[4]
        self.z2 = data[5]
        print(f"Got a first tuple: {data}")
        print(f"It includes: X={self.x}, Y={self.y}, Z={self.z}")

    def display_distance(self) -> None:
        distance: float = math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2 + (self.z2-self.z1)**2)
        print(f"Distance to center: {distance}")


def get_player_pos() -> tuple[int]:
    arg_list: list[int] = []
    user_input: str = input(
        "Enter new coordinates as floats"
        " in format 'x,y,z': "
    )
    if ',' not in user_input:
        print(invalid_syntax)
    for arg in user_input.split(","):
        try:
            arg_list.append(float(arg))
        except ValueError:
            raise ValueError(
                f"Error on parameter '{arg}':"
                f"could not convert string to float: '{arg}'"
            )
    if len(arg_list) > 3:
        raise invalid_syntax
    return tuple(arg_list)


if __name__ == "__main__":
    end: int = 0
    while (1):
        try:
            position_1: tuple[int] = get_player_pos()
            position_2: tuple[int] = get_player_pos()

        except (ValueError, invalid_syntax) as e:
            print(f"{e}")


