# Average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
total_count = 0
for i in range(0, len(student_heights)):
    total_height += student_heights[i]
    total_count += 1
average_height = total_height / total_count
print(round(average_height))
