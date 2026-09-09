str_a = input("Enter a number as digits: ")
str_b = input("Enter a number as digits: ")

a = int(str_a)
b = int(str_b)

def addition(a, b):
    add = a + b
    return add
addVariable = addition(a,b)

def subtraction(a, b):
    subtract = a - b
    return subtract
subtractVariable = subtraction(a,b)

def multiplication(a,b):
    multiply = a * b
    return multiply
multiplyVariable = multiplication(a,b)

def division(a,b):
    divide = a/b
    return divide
divideVariable = division(a,b)

choice = input("""
What operation do you want to perform?
1 addition
2 subtraction
3 multiplication
4 division
5 all four operations
""")

if choice == "1" or choice == "addition":
    print(f"Addition of {a} and {b} is {addVariable}")
elif choice == "2" or choice == "subtraction":
    print(f"Subtraction of {a} and {b} is {subtractVariable}")
elif choice == "3" or choice == "multiplication":
    print(f"Multiplication of {a} and {b} is {multiplyVariable}")
elif choice == "4" or choice == "division":
    print(f"Division of {a} and {b} is {divideVariable:.3f}")
elif choice == "5" or choice == "all four operations":
    print(f"""
    All arithmetic operations of {a} and {b}:
Addition: {addVariable}
Subtraction: {subtractVariable}
Multiplication: {multiplyVariable}
Division: {divideVariable:.3f}     
""")    

