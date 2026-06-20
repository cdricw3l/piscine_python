if __name__ == "__main__":
    print(f"=== Game Data Alchemist ===\n")
    player_list: list[str] =  ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {player_list}")
    capitalize_list : list[str] = [player.capitalize() for player in player_list]
    print(f"New list with all names capitalized: {capitalize_list}")
    capitalized_only_list : list[str] = [player for player in player_list if player == player.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only_list}")