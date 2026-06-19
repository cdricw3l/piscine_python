import math


class Invalid_syntax(Exception):
    def __init__(self, msg: str = "Invalid syntax") -> None:
        Exception.__init__(self, msg)


class Set_data():
    __points: tuple[float, ...]

    def __init__(self, points: tuple[float, ...]) -> None:
        self.__points = points

    def display_set_data(self) -> None:
        print(f"Got a first tuple: {self.__points}")
        print(
            f"It includes: X={self.__points[0]},"
            f"Y={self.__points[1]},"
            f"Z={self.__points[2]}"
        )

    def display_distance(self) -> None:
        distance: float = math.sqrt((self.__points[0])**2
                                    + (self.__points[1])**2
                                    + (self.__points[2])**2
                                    )
        print(f"Distance to center: {round(distance, 4)}\n")

    def get_set(self) -> tuple[float, ...]:
        return tuple(self.__points)


def distance_between_two_set(set_1: Set_data, set_2: Set_data) -> None:
    s1: tuple[float, ...] = set_1.get_set()
    s2: tuple[float, ...] = set_2.get_set()
    print(s1)
    print(s2)
    distance: float = math.sqrt((s2[0] - s1[0])**2
                                + (s2[1] - s1[1])**2
                                + (s2[2] - s1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


def get_player_pos() -> tuple[float, ...]:
    arg_list: list[float] = []

    while (1):
        user_input: str = input(
            "Enter new coordinates as floats"
            " in format 'x,y,z': "
        )
        if ',' not in user_input:
            raise Invalid_syntax
        for arg in user_input.split(","):
            try:
                arg_list.append(float(arg))
            except ValueError as e:
                raise ValueError(f"Error on parameter '{arg}': {e}")
        if len(arg_list) > 3:
            raise Invalid_syntax
        return tuple(arg_list)

#input getter whith label printing
def get_set(label: str) -> tuple[float, ...]:
    print(f"Get a {label} set of coordinates")
    # infinit loop utils good set
    while 1:
        try:
            set: tuple[float, ...] = get_player_pos()
            return set
        except (Invalid_syntax, ValueError) as e:
            print(f"{e}")


if __name__ == "__main__":
    set_1: tuple[float, ...] = get_set("first")
    data_set_1: Set_data = Set_data(set_1)
    data_set_1.display_set_data()
    data_set_1.display_distance()
    set_2: tuple[float, ...] = get_set("second")
    data_set_2: Set_data = Set_data(set_2)
    distance_between_two_set(data_set_1, data_set_2)
