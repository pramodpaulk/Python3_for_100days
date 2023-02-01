#Even or Odd number
number = int(input("Which number do you want to check? "))

if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

def bmi_calculator(height, weight):
    bmi = weight / pow(height,2)
    return round(bmi)

bmi = bmi_calculator(height, weight)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#Leap Yearcomputer
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
   if year % 100 !=0 or year % 400 == 0:
       print("Leap year.")
   else:
       print("Not leap year.")
else:
    print("Not leap year.")

# Automatic pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
pizza_size = {'S':15,'M':20,'L':25}
toppings = {'S':2,'M':3,'L':3}
Total = 0
user_input = [size, add_pepperoni, extra_cheese]
Total += pizza_size[size]
if add_pepperoni == 'Y':
    Total += toppings[size]
if extra_cheese == 'Y':
    Total += 1
print(f"Your final bill is: ${Total}.")