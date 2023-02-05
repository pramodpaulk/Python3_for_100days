"""Datatypes and string manipulation"""

# Type conversion and adding two individual digits
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Life in Weeks
age = input("What is your current age? ")
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
hours_left = days_left * 24
minutes_left = hours_left * 60
seconds_left = minutes_left * 60
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
message1 = f"You have {hours_left} hours, {minutes_left} minutes, and {seconds_left} seconds left."
print(message)
print(message1)


# BMI Calculator
def bmi_calculator():
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    bmi = float(weight) / pow(float(height), 2)
    print(int(bmi))
