import random

class Pick_achivement_error(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)

class Achivement_data():
    __achivement_set: set

    def __init__(self, achivement_set: set) -> None:
        self.__achivement_set = achivement_set

    def get_achivement(self) -> set:
        return (set(self.__achivement_set))

    def __str__(self):
        return f"All distinct achievements: {self.__achivement_set}"

class Player():
    __name: str
    __player_achivement: set
    _number_of_achivement: int
    

    def __init__(self, name: str, number_of_achivement: int) -> None:
        self.__name = name
        self._number_of_achivement = number_of_achivement
        self.__player_achivement = set()

    def pick_achivement(self, achivement_set: set[str]) -> None:
        for i in range(self._number_of_achivement):
            # avoid dupplicate achivement
            random_achivment: str = random.choice(tuple(achivement_set))

            while random_achivment in self.__player_achivement:
                #print(f"we can't have dupplicate achivement {random_achivment}")
                random_achivment = random.choice(tuple(achivement_set))
            self.__player_achivement.add(random_achivment)

    def get_achivement(self) -> set:
        return (set(self.__player_achivement))
    
    def get_name(self) -> str:
        return (self.__name)

    def __str__(self) -> str:
        return f"Player {self.__name}: {self.__player_achivement}"
        
# achivement inherite form player 
class Achivement(Achivement_data):

    _players: list[Player]

    def __init__(self, players: list[str], achivement_set: set[str], number_of_achivement_to_pk: int) -> None:
        #if the number of achivement to pick is biggest than the achivement set -> err

        if number_of_achivement_to_pk > len(achivement_set):
            raise  Pick_achivement_error(f"the number of chivement to pick is biggest than the achivement set, max achivement: {len(achivement_set)}")
        #achivement data class initialisation
        Achivement_data.__init__(self, achivement_set)
        self._players = []
        for player in players:
            p: Player = Player(player, number_of_achivement_to_pk)
            # get achivement from parent class Achivement_data
            p.pick_achivement(self.get_achivement())
            self._players.append(p)
    
    def get_all_player_achivement(self) -> dict[str,set]:
        common_set: dict[str,set] = {}
        for player in self._players:
            common_set.update({player.get_name(): player.get_achivement()})
        return common_set

    def display_player_achivement(self) -> None:
        for player in self._players:
            print(f"{player}\n")
    
    def display_all_achivement(self) -> None:
        print(f"All distinct achievements: {self.get_achivement()}\n")

    def diplay_common_achivement(self) -> None:
        common_set: dict[str,set] = self.get_all_player_achivement()
        common_set_value: list[set] = list(common_set.values())
        # * is the variadique way
        print(f"Common achievements: {set(common_set_value[0]).intersection(*common_set_value[1:])}\n")

    def only_has_achivement(self) -> None:
        common_set: dict[str,set] = self.get_all_player_achivement()
        common_set_value: list[set] = list(common_set.values())
        for player, i in self._player:
            print(f"{player}")


if __name__ == "__main__":

    #ach = set({'Crafting Genius', 'Strategist', 'World Savior'})
    player_list: list[str] = ["cedric", "michel", "loic"]
    achivement_list = set({'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', \
            'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', \
            'Untouchable', 'Sharp Mind', 'Boss Slayer'})
    nb_of_achiv_to_pick: int = 5
    try:
        p1 : Achivement =  Achivement(player_list, achivement_list, nb_of_achiv_to_pick)
        print(p1.get_all_player_achivement())
        p1.display_player_achivement()
        p1.display_all_achivement()
        p1.diplay_common_achivement()
    except Pick_achivement_error as e:
        print(f"{e}")
