# Main File

from components import player_info
from components import intro

def main():
    info = player_info.user_info()
    user_choice = intro.intro(info)

    # Running the game

main()
