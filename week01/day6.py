#1 Searching student in list (using found boolean condition)
student_name = input("Enter student name: ")
students = ["Shawn", "Brian", "Abdullahi", "Samuel"]
found = False

for student in range(0, len(students), 1):
    if student_name == students[student]:
        found = True
        print(f"{student_name} is in students list")
        break    
if found == False:
    print(f"{student_name} is not in students list")


#2 Searching student in list (using else)
student_name = input("Enter student name: ")
students = ["Shawn", "Brian", "Abdullahi", "Samuel"]

for index_student in range(0, len(students), 1):
    if student_name == students[index_student]:
        print(f"{student_name} is in students list")
        break    
else:
    print(f"{student_name} is not in students list")


#3 Searching student + score
info = input("Enter student name: ")
students =[
  ["Shawn", 72],
  ["Alex", 85],
  ["Abdullahi", 64],
  ["Brian", 91],  
  ["Samuel", 78]
]

for student in range(0, len(students), 1):
  if info == students[student][0]:
    name = students[student][0]
    score = students[student][1]
    print(f"{name} has {score} marks")
    break
else:
  print(f"{info} is not in list")    