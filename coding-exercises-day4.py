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
random_index = random.randint(0, len(names))
print(f"{names[random_index]} is going to buy the meal today!")