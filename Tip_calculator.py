#Tip Calculator
print("***Welcome to the tip calculator***")
total_bill = eval(input("What was the total bill\n$"))
total_people = eval(input("How many people to split the bill?\n"))
tip_percentage = eval(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
total_incl_tip = total_bill * (1 + tip_percentage/100)
indiviual_split = "{:.2f}".format(total_incl_tip / 5)
print(f"Each person should pay:${indiviual_split}")
