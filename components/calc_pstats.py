# Player Stats Calculation

from player import listed_class, player_classes, player_stats


def calc_stat():
    pstat = player_stats.player_stats()
    classes = player_classes.player_classes()
    c_list = listed_class.listed_class()

    while True:
        print("Available Classes: ")
        for num, c_name in enumerate(c_list, start=1):
            print(f"{num}. {c_name}")

        while True:
            try:
                pick_class = int(input("Pick the number of your class: "))
                chosen_class = pick_class - 1

                if chosen_class >= 0 or chosen_class == len(c_list):
                    print(f"You selected {chosen_class}!")

                    dict_key = f"class{chosen_class}"
                    added_stats = classes[dict_key]

                    for stat, value in added_stats.items():
                        if stat == "ClassName":
                            pstat["Class"] = value

                        elif stat in pstat:
                            pstat[stat] += value

                    print(pstat)
                    return pstat

                else:
                    print(f"Input cannot exceed {len(c_list)}")
                    continue
            except ValueError:
                print("Invalid Input.")
                continue