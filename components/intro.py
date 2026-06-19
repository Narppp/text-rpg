# Game Introduction


def intro(info):
    player = info.get("Name", None)
    options = ["Tutorial", "Play Game", "Options", "Patch Notes", "Exit"]
    print(f"Welcome to my Text RPG Game, {player}!")
    print("Date Made: June 17, 2026")
    while True:
        for num, option in enumerate(options, start=1):
            print(f"{num:>10}. {option.upper():>10}")

        try:
            player_choice = int(
                input("Please choose the number of the option you'd like: ")
            )
            player_choice = player_choice - 1

            if player_choice < 0:
                print("Invalid Option.")
                continue
            else:
                return options[player_choice]
        except ValueError:
            print("Invalid Input.")
            continue
        except IndexError:
            print("Invalid Option.")
            continue
