# Average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
total_count = 0
for height in student_heights:
    total_height += height
    total_count += 1
average_height = total_height / total_count
print(round(average_height))

'''Getting the highest score of a student from the list'''
# highest score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# Sum of even numbers in 1-100
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

''' Every multiple of 3 is fizz and multiple of 5 is buzz and multiple of both is FizzBuzz '''
# FizzBuzz
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        number = "FizzBuzz"
        print(number)
    elif number % 3 == 0:
        number = "Fizz"
        print(number)
    elif number % 5 == 0:
        number = "Buzz"
        print(number)
    else:
        print(number)