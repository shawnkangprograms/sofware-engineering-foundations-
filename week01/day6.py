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


#4 Evaluating transactions
transactions = [
    ["Monday", 450],
    ["Tuesday", 1200],
    ["Wednesday", 300],
    ["Thursday", 850],
    ["Friday", 1500]
]

min_transaction = int(input("Enter minimum transaction: "))

highest_day = None
highest_transaction = 0
count = 0
total = 0

for transaction in range(0, len(transactions), 1):
  if transactions[transaction][1] >= min_transaction:
    count = count + 1
    total = total + transactions[transaction][1]
    if highest_transaction < transactions[transaction][1]:
      highest_transaction = transactions[transaction][1]
      highest_day = transactions[transaction][0]

if count == 0:
  print("There are no qualifying transactions")

if count != 0:  
  print(f"""
  Highest transaction was {highest_transaction} on {highest_day}
  Count of qualified transactions is {count}
  Total of qualified transactions is {total}
  """)


#5. Retrieving student scores
results = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64],
    ["Brian", 91],
    ["Samuel", 58],
    ["Mary", 76]
]

min_passing = int(input("Enter minimum passing mark: "))

highest_student = 0
count = 0
total = 0

for result in range(0, len(results), 1):
    if results[result][1] >= min_passing:
        count = count + 1
        total = total + results[result][1]
        
        if highest_student < results[result][1]:
            highest_student = result[results][1]
            name = result[results][0]
            
    if count == 0:
        print("No one has passed.")
        
    if count != 0:
        print (f"""
            Count of passing students is {count}
            Total score of passing students is {total}
            Student with highest mark is {name} with {highest_student} marks
        """)