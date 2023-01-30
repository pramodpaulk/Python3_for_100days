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

