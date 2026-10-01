#1 identifying missing numbers in list
inputs = [0,1,2,3,5,6,7,8,9]
completes = [0,1,2,3,4,5,6,7,8,9]
counter = 0

for complete in completes:
    found = False
    for input in inputs:
      counter = counter + 1
      if input == complete:
        found = True
        break
    if found == False:
      print(f"Missing number is {complete}. We've iterated {counter} times") 
      continue


#2 defining and calling functions
def total_number(numbers):
  total = 0
  for number in numbers:
    total = total + number
  return total

value = total_number([2,4,6])
valueTwo = total_number([100,200,300]) 
valueThree = total_number([7,3,9,1])
print(f"{value}\n{valueTwo}\n{valueThree}")

#3 storing and unpacking multiple function parameters
def arithmetic(first, second):
  sum = first + second
  diff = first - second
  return sum, diff
sum, diff = arithmetic(1,2)
print(f"Sum: {sum} \n Diff: {diff}")

#4. finding negative number
numbers = [4, 7, 2, 9] 
def negativeDetector(numbers): 
  for number in numbers: 
    if number < 0:
      return number
  return None    
negative = negativeDetector(numbers) 
if negative is not None : 
  print(f"List contains negative number {negative}") 
elif negative is None: 
  print("List doesn't contain negative number")