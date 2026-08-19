#Part 1. The 4 fundamental data types 

name="chat"
age=22
height=1.68
is_student=True

print("Part 1. The 4 fundamental data types ")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Part 2: Strings aren't numbers
x = "10"
y = 10

print("Part 2: Strings aren't numbers")
print(type(x))
print(type(y))
print(x+x)
print(y+y)

#Part 3: Type Conversion
x = "10"
y = int(x)
z = str(y)

print("Part 3: Type Conversion")
print(type(x))
print(type(y))
print(type(z))

#Part 4: Experiment
print("Part 4: Experiment")
x = "25"
print(type(x))

x= int(x)
print(type(x))

x = float(x)
print(type(x))

x = str(x)
print(type(x))

#Part 5: Arithmetic operators 
print("Part 5: Arithmetic Operators")
addition=10+3
subtraction=10-3
multiplication=10*3
division=10/3
floorDivision=10//3
modulus=10%3
print(f"""
addition: {addition}
subtraction: {subtraction}
mutliplication: {multiplication}
division: {division:.4f}
floor division: {floorDivision}
modulus: {modulus}
""")

# Skipped part 6(modulus) because its covered in part 5

# Part 7: Comparison Operators
print("Part 7: Comparison Operators")
equality = 10==5
notEqual = 10!=5
moreThan = 10>5
lessThan = 10<5
MoreOrEqual = 10>=5
LessOrEqual = 10<=5 

print (f"""
Equality: {equality}
Not Equal: {notEqual}
More Than: {moreThan}
Less Than: {lessThan}
More or Equal: {MoreOrEqual}
Less or Equal: {LessOrEqual}
""")

# Part 8: = vs ==
print("Part 8: = vs ==")
age = 21
print(f"Age: {age}")
isTwentyOne = (age == 21)
print(f"Age: {isTwentyOne}")

# Part 9: Logical Operators
print("Part 9: Logical Operators")
if age > 18 and age < 30:
    print("valid age")
elif age < 18 and age > 65:
    print("Invalid age") 
else:
    print("An error occured")       