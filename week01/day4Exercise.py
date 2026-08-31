# Exercise 1 - Basic Function
def greet():
    name = input("What's your name? ")
    return name

print("Before")
greetVariable = greet()
print(f"{greetVariable}")
print("After")

#Exercise 2 - Arithmetic Function (addition)
def arithmetic(a, b):
    str_a = input("Enter the first number: ")
    str_b = input("Enter the second number: ")
    a = int(str_a)
    b = int(str_b)

    result = a + b
    return result

arithmeticVariable = arithmetic(1,2)
print(f"Addition: {arithmeticVariable}")

#Exercise 3 - Arithmetic Function (same as Exercise 2)
arithmeticVariableB = arithmetic(8,9)
print(f"Addition {arithmeticVariableB}")

#Exercise 4 - Multi-arithmetic function
#subtraction
str_c = input("Enter the first number: ")
str_d = input("Enter the second number: ")
c = int(str_c)
d = int(str_d)
def subtraction(c, d):
    subtract = c - d
    return subtract

subtractionVariable = subtraction(1,2)
print(f"Subtraction {subtractionVariable}")

#multiplication
str_e = input("Enter the first number: ")
str_f = input("Enter the second number: ")
e = int(str_e)
f = int(str_f)
def multiplication(e, f):
    multiply = e * f
    return multiply

multiplicationVariable = multiplication(1,2)
print(f"Multiplication: {multiplicationVariable}")

#DIVISION
str_g = input("Enter the first number: ")
str_h = input("Enter the second number: ")
g = int(str_g)
h = int(str_h)
def division(g, h):
    divide = g / h
    return divide

divisionVariable = division(1,2)
print(f"Division {divisionVariable:.2f}")

#modulus division
str_i = input("Enter the first number: ")
str_j = input("Enter the second number: ")
i = int(str_i)
j = int(str_j)
def modulus_division(i, j):
    modulusDivide = i % j
    return modulusDivide

modulusDivideVariable = modulus_division(1,2)
print(f"Modulus Division: {modulusDivideVariable}")


# next experiment - observing parameter behavior
def getIdentification(name, age, phone_number):
    name = input("What's your name? ")
    str_age = input("What's your age? ")
    age = int(str_age)
    phone_number = input("What's your phone number? ")

    identification = (f"{name}, {age}, {phone_number}")
    return identification

idVariable = getIdentification("shawn", 11, 12345)
print (f"Identification: {idVariable}")

# experiment 2: print vs return test
def printTest():
    name=input("Enter your name: ")
    printTesting = print(f"{name}")

    return printTesting

printTestVariable = printTest()

def returnTest():
    name=input("Enter your name: ")
    returnTesting = name

    return returnTesting

returnTestVariable = returnTest()
