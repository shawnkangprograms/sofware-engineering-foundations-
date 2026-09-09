# MAIN EXERCISE

students = [
    ["Shawn", 72],
    ["Alex", 85],
    ["Abdullahi", 64],
    ["Brian", 91],
    ["Samuel", 78]
]

highest_name = students[0][1]
lowest_name = students[0][1]
highest_score = students[0][1]
lowest_score = students[0][1]
total = 0
count = 0

for student in students:
  # highest and lowest scoring student
  if highest_score < student[1]:
    highest_score = student[1]
    highest_name = student[0]
  if lowest_score > student[1]:
    lowest_score = student[1]
    lowest_name = student[0]
  # total of all scores
  total = total + student[1]
  # how many students scored 70 and above
  if student[1] >= 70:
    count = count + 1
  
print(f"""
  Highest Scoring Student:
  {highest_name} : {highest_score}

  Lowest Scoring Student:
  {lowest_name} : {lowest_score}

  Total of all scores:
  {total}

  Students that scored 70 and above:
  {count}
  """)  


# ASSESSMENT