#Calculate the average height of the students. 
#Write a series of student heights in centimeters separated only by a space. Do not use periods or commas. Example: 184 178 191 182.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for  height  in  student_heights:
  total_heights += height
print(total_heights)

total_students = 0
for  student in student_heights:
  total_students += 1
print(total_students)

average_student_height = round(total_heights / total_students)
print(average_student_height)