# identifying missing numbers in list
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


# defining and calling functions
def total_number(numbers):
  total = 0
  for number in numbers:
    total = total + number
  return total

value = total_number([2,4,6])
valueTwo = total_number([100,200,300]) 
valueThree = total_number([7,3,9,1])
print(f"{value}\n{valueTwo}\n{valueThree}")