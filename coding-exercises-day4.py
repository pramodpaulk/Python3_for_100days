# Virtual coin toss
import random
result = random.randint(0, 1)
if result == 0:
    print("Tails")
else:
    print("Heads")

# Banker Roulette
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_index = random.randint(0, len(names)-1)
print(f"{names[random_index]} is going to buy the meal today!")

# Treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
map[int(position[1]) - 1][int(position[0]) - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")

