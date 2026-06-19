# Main File

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from components import intro, player_info  # noqa: E402


def main():
    info = player_info.user_info()
    user_choice = intro.intro(info)

    # Running the game


main()
