# Patch Notes

def patch():
    print("""Text RPG 1.0 (Beta):
    - Added Getting Player Info
    - Added Introduction
    - Added Default Player Stats
    - Added Classes""")

    while True:
        exit_program = input("Exit Section? (y/n): ").lower()

        if exit_program in ["y", "yes"]:
            return
        elif exit_program in ["n", "no"]:
            continue
        else:
            print("Invalid Option.")
            continue

