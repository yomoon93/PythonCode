import random

def setup_doors():
    lst = ["GOAT", "GOAT", "GOAT"]
    lst[random.randint(0, 2)] = "CAR"
    return lst

def except_list(n):
    return [x for x in range(0, 3) if x != n]

doors = setup_doors()
#print(doors)

choice = int(input("Choose a door (0, 1, or 2): "))

otherDoors = except_list(choice)
if doors[otherDoors[0]] == "GOAT" and doors[otherDoors[1]] == "CAR":
    doors[otherDoors[0]] = "OPEN"
elif doors[otherDoors[0]] == "CAR" and doors[otherDoors[1]] == "GOAT":
    doors[otherDoors[1]] = "OPEN"
else:
    randomDoor = random.randint(0, 1)
    doors[otherDoors[randomDoor]] = "OPEN"

#print(doors)

changeOrNot = input("Do you want to change? (Yes or No)")
change = True if changeOrNot == "Yes" else False

if (change and doors[choice] == "GOAT") or (not change and doors[choice] == "CAR"):
    win = True
else:
    win = False

print(win)