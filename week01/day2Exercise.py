# ask user for name, age, and height

name= input("Hey there! What's your name? ")
while not name.isalpha():
    print("You know names only consist of letters, right?")
    name= input("Enter your name. Seriously this time. ")
thanks=(f"Thanks for your input, {name}") 
print(f"{thanks}")   

age= (input("What's your age? "))
while not age.isdigit():
    print("I'll need your age as a number")
    age= input("Enter your age: ")
age=int(age)    
if age < 0 or age > 125:
    print("Either you don't know the concept of age or you should pay a visit to the Guiness Book of World Records")
    age=(input("Enter your age. Seriously this time: "))  
    age=int(age)
elif age < 5:
    print("Sorry, you're too young to use this program. ")
else:
    print("Welcome! Your good to go.")      
print(f"{thanks}")   

while True:
    try:
        height = float(input("What's your height in metres? "))
        if height < 0 or height > 4:
            print("Either you don't know the concept of height or you should pay a visit to the Guiness Book of World Records")  
            continue
        break
    except ValueError:    
        print("I'll need your height as a number")
   
print(f"{thanks}")   


# calculate age in months and days
ageMonths= age*12
ageDays= age*365

# calculate height in centimetres
heightCm= height*100

print (f"""
Hey {name}! 
You inputted your age as {age} years.
That's equivalent to {ageMonths} months and {ageDays} days.
That's a lot, right?
You also inputted your height as {height} metres.
That's equivalent to {heightCm} centimetres.
""")

# determine whether their age is even and if they are between 18 and 25

if age % 2 == 0:
    print("Your age is even")
elif age % 2 == 1:
    print("Your age is odd")
else:
    print("Something went wrong")    

if age >= 18 and age <= 25:
    print("You're between 18 and 25: True")   
else:
    print("You're between 18 and 25: False")         


# Part 11: Challenge
print("Program 2")
raw_number_one = input(f"Enter the first integer {name}: ")
while not raw_number_one.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_number_one = input("Enter any integer. ")
first_number = int(raw_number_one) 

raw_number_two = input("Enter the second integer: ")
while not raw_number_two.isdigit():
    print("Invalid input! Please enter digits only.")
    raw_number_two = input("Enter any integer. ")
second_number = int(raw_number_two)  

if first_number > second_number:
    print(f"{first_number} is larger than {second_number}")
else:
    print(f"{second_number} is larger than {first_number}")

if first_number < second_number:
    print(f"{first_number} is smaller than {second_number}")
else:
    print(f"{second_number} is smaller than {first_number}")

if first_number == second_number:
    print(f"{first_number} is equal to {second_number}")
else:
    print("An error occurred")

sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
division = first_number / second_number
remainder = first_number % second_number
firstNumberEven = first_number % 2 == 0
secondNumberEven = second_number % 2 == 0

print(f"""
Their sum: {sum}
Their difference: {difference}
Their product: {product}
Their division: {division}
Their remainder: {remainder}
Is first number even? {firstNumberEven}
Is second number even? {secondNumberEven}
""")        