'''Datatypes and string manipulation'''

#Type conversion and adding two individual digits
two_digit_number = input("Type a two digit number: ")
print(int(str(two_digit_number[0])) + int(str(two_digit_number[1])))

#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / pow(float(height),2)
print(int(bmi))
