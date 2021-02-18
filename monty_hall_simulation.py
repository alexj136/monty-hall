import random

SHOULD_STICK = 0
SHOULD_SWITCH = 1

def choose_door_host_opens(goat_doors, pick):
    if pick not in goat_doors:
        return random.choice(goat_doors)
    goat_doors_copy = goat_doors.copy()
    goat_doors_copy.remove(pick)
    return goat_doors_copy[0]

def door_not_picked_or_opened(pick, door_host_opens):
    possible_picks = [0, 1, 2]
    possible_picks.remove(pick)
    possible_picks.remove(door_host_opens)
    return possible_picks[0]

def run():
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    goat_doors = [door_num for door_num, door_contents in enumerate(doors) if door_contents == "goat"]
    pick = random.randint(0, 2)
    door_host_opens = choose_door_host_opens(goat_doors, pick)
    return SHOULD_SWITCH if doors[door_not_picked_or_opened(pick, door_host_opens)] == "car" else SHOULD_STICK

if __name__ == '__main__':
    runs = 100
    should_switches = 0
    for x in range(runs):
        should_switches += run()
    print("Should have stuck " + str(runs - should_switches) + " times.")
    print("Should have switched " + str(should_switches) + " times.")
