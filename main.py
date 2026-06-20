# Main File

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from components import intro, player_info  # noqa: E402
from components.options import exit, options, patch_notes, play, tutorial  # noqa: E402
from components.player import player_classes, player_stats  # noqa: E402

def main():
    info = player_info.user_info()

    while True: 
        user_choice = intro.intro(info)
        if user_choice == "Tutorial":
            pass
        elif user_choice == "Play Game":
            pass
        elif user_choice == "Options":
            pass
        elif user_choice == "Patch Notes":
            patch_notes.patch()
        else:
            exit()

    # Running the game


main()
