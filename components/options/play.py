# Playing the game

from components import calc_pstat


def play_game():
    player_class = calc_pstat.calc_stat()

    print(f"Chosen class: {player_class}")
