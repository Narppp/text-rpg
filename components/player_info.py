# Getting User Info

def user_info():
    while True:
        player = {}
        player_name = input("Create your username: ").title()
        
        if player_name.replace(" ", "").isalpha():
            print(f"Welcome {player_name}!")
        else:
            print(f"{player_name} is an invalid name, try again.")
            continue

        joined_name = " ".join(player_name.split())
        player["Name"] = joined_name

        while True:
            try:
                player_age = int(input("Enter your age: "))
                if player_age < 13:
                    print("You are too young to be playing this game.")
                    del player
                    break
                elif player_age < 18:
                    confirm = input("This game is only for 18+ users, are you sure you want to enter? (y/n): ").lower()
                    if confirm in ["y", "yes"]:
                        player["Age"] = player_age
                        return player
                    elif confirm in ["n", "no"]:
                        del player
                        break
                    else:
                        print("Invalid option.")
                        continue
                else:
                    player["Age"] = player_age
                    return player
            except ValueError:
                print("Invalid input, try again.")
                continue
