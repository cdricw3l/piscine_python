import random


class Random_generation_error(ValueError):
    msg: str = "Achivement len list is equal to zero: add achivements!"

    def __init__(self, msg: str = msg):
        Exception.__init__(self, msg)


class Player_generation_error(ValueError):
    msg: str = "Players list is empty: add players!"

    def __init__(self, msg: str = msg):
        Exception.__init__(self, msg)


class Player:
    __achivements: set[str]
    __name: str

    def __init__(self, name: str, achivements: set[str]) -> None:
        self.__name = name.capitalize()
        self.__achivements = achivements

    def get_name(self) -> str:
        return self.__name

    def get_achivements(self) -> set[str]:
        return self.__achivements


class Achivement:
    __players: list[Player]
    __all_achivements: set[str]

    def __init__(self, player_list: list[str],
                 achivement_list: list[str],
                 nba: int) -> None:
        if len(player_list) == 0:
            raise Player_generation_error
        self.__all_achivements = set(achivement_list)
        self.__players = []
        for player in player_list:
            achivements: set[str] = gen_player_achievements(
                achivement_list, nba)
            new_player: Player = Player(player, achivements)
            self.__players.append(new_player)

    def display_players_achivement(self) -> None:
        for player in self.__players:
            print(
                f"Player: {player.get_name()}: {player.get_achivements()}"
            )

    def display_all_achivements(self) -> None:
        print(
            f"All distinct achievements: {self.__all_achivements}"
        )

    def commun_achivements(self) -> None:
        set_list: list[set[str]] = []
        for p in self.__players:
            set_list.append(p.get_achivements())
        commun: set[str] = set.intersection(*set_list[0:])
        print(f"Common achievements: {commun}")

    def only_has_achivements(self) -> None:
        # nested loop for creating player set and set other set
        for p in self.__players:
            other_list: list[set[str]] = []
            player_list: list[set[str]] = []
            for x in self.__players:
                name: str = p.get_name()
                if name != x.get_name():
                    other_list.append(x.get_achivements())
                else:
                    player_list.append(p.get_achivements())
            only_has: set[str] = set(player_list[0])\
                .difference(*other_list[0:])
            print(f"Only {name} has: {only_has}")

    def missing_achivement(self) -> None:
        for p in self.__players:
            missing: set[str] = set(self.__all_achivements)\
                .difference(p.get_achivements())
            print(f"{p.get_name()} is missing: {missing}")


def gen_player_achievements(achivements: list[str], nba: int) -> set[str]:
    player_set: set[str] = set(random.sample(achivements, nba))
    return set(player_set)


def gen_ramdom_set_size(achivement_list: list[str]) -> int:
    try:
        nba: int = random.randrange(1, len(achivement_list))
    except ValueError:
        raise Random_generation_error
    return nba


if __name__ == "__main__":
    player_list: list[str] = ["cedric", "michel", "loic", "jaque"]
    achivement_list: list[str] = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']

    try:
        nba: int = gen_ramdom_set_size(achivement_list)
        achivement: Achivement = Achivement(player_list, achivement_list, nba)
        print("=== Achievement Tracker System ===\n")
        achivement.display_players_achivement()
        print()
        achivement.display_all_achivements()
        print()
        achivement.commun_achivements()
        print()
        achivement.only_has_achivements()
        print()
        achivement.missing_achivement()
    except (Random_generation_error, Player_generation_error) as e:
        print(e)
