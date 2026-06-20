# Listed classes

import player_classes


def listed_class():
    classes = player_classes.player_classes()

    swordsman = classes.get("class1", {}).get("ClassName", None)
    mage = classes.get("class2", {}).get("ClassName", None)
    tank = classes.get("class3", {}).get("ClassName", None)

    class_list = [swordsman, mage, tank]

    return class_list
