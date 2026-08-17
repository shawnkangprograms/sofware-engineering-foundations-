# 1. printing name and age

first_name = input("Hello there! Enter your first name: ")
while not first_name.isalpha():
    print("Invalid input! First names only have letters in them, in case you weren't taught")
    first_name = str(input("Enter your first name. Seriously this time. "))

last_name = input("I'll also need your last name: ")
while not last_name.isalpha():
    print("Invalid input! Last names only have letters in them, in case you weren't taught")
    last_name = input("Enter your last name, " + first_name + ". Seriously this time. ")

print("Thanks for your input " + first_name + " " + last_name + "!")

raw_input = input("Hi " + first_name + "! Could you input your age for no reason at all? " )

while not raw_input.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_input = input("Enter your age: ")

age = int(raw_input)    
print("I will now guess your age " + last_name +". You're " + str(age) +" years old!")


# performing arithmetic

raw_number_one = input("Enter the first integer " + first_name + ": ")
while not raw_number_one.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_number_one = input("Enter any integer. ")
first_number = int(raw_number_one) 

raw_number_two = input("Enter the second integer: ")
while not raw_number_two.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_number_two = input("Enter any integer. ")
second_number = int(raw_number_two)

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = (first_number / second_number)

print (f"Arithmetic of {first_number} and {second_number} :")
print(f"""
Addition: {addition} 
Subtraction: {subtraction} 
Multiplication: {multiplication} 
Division: {division:.4f} 
""")


# 2. calculating area of rectangle
raw_length = input("Enter the length of the rectangle " + first_name + ": ")
while not raw_length.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_length = input("Enter length as a digit. ")
length = int(raw_length) 

raw_width = input("Enter the width of the rectangle: ")
while not raw_width.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_width = input("Enter width as a digit. ")
width = int(raw_width)

area = length * width

print (f"Area of rectangle length {length} and width {width} is {area}")
