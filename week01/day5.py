
#1. Creating and acessing lists
students = ["Shawn", "Alex", "Abdullahi", "Brian", "Samuel"]

one = students[0]
print(f"{one}")

third  = students[2]
print(f"{third}")

last = students[-1]
print(f"{last}")

number = len(students)
print(f"{number}")

original_list = print(students)

students[1] = "Mary"
students[-1] = "David"

modified_list = print(students)

new_number = len(students)
print(new_number)

students.append("Brian")
print(students)

students.insert(2, "Kevin")
print(students)

students.remove("Kevin")
print(students)

value = students.pop(2)
print(students)
print(value)

students.pop(-1)
print(students)

last = students.pop()
print(students)
print(last)

students.sort()
print(students)

students.reverse()
print(students)

for student in students:
    print(student)

students = ["Shawn", "Mary", "Abdullahi", "Brian"]
if "Kevin" in students:
    print("Kevin is a student")
else:
    print("Kevin is not a student") 


#2 tallying items in a list
scores = [72, 85, 64, 91, 78]      
total = 0
for score in scores:
    total = score + total
print(total)          


#3 getting highest and lowest score without max or min
scores = [72, 85, 64, 91, 78]
highest_score = scores[0]

for score in scores:
  if highest_score < score:
    highest_score = score
print(highest_score)

scores = [72, 85, 64, 91, 78]
lowest_score = scores[0]

for score in scores:
  if lowest_score > score:
    lowest_score = score
    print(lowest_score)      


#4. Counting scores >= 70
scores = [72, 85, 64, 91, 78, 55, 90, 63]
equal_higher = 0

for score in scores:
   if score < 70:
      equal_higher = equal_higher
      continue
   elif score >= 70:
      equal_higher = equal_higher + 1
print(equal_higher)      


#5. Acessing nested lists
students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]
for student in students:
    print(student[0])

students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]
for student in students:
    print(student[1])


#6. Calculating total in a nested list
students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]
total = 0

for student in students:
    total = total + student[1]
print(total)    


#7. Calculating lowest and highest score in a nested list
students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]
highest_score = students[0][1]
lowest_score = students[0][1]

for student in students:
  if highest_score < student[1]:
    highest_score = student[1]
  if lowest_score > student[1]:
    lowest_score = student[1]
print(highest_score)
print(lowest_score)
    

#8. Printing student name and score

students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]

for student in students:
    print(f"{student[0]} scored {student[1]}")


#9. Finding the name associated with the highest value

students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64]
]

highest_score = students[0][1]
name = students[0][0]

for student in students:
    if highest_score < student[1]:
      highest_score = student[1]
      name = student[0]
print(name)   


#10. Searching students in a list

ask = input("Enter student name: ")

students = ["Shawn", "Alex", "Abdullahi", "Brian", "Samuel"]

for student in students:
  if ask == student:
    print(f"{ask} is in the list")
    break
else:
  print(f"{ask} is not in the list")    