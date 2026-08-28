while True:
    try:
        name= input("Input your name: ")
        if not name.isalpha():
            print ("You know names only consist of letters, right?")
            continue
        break
    except ValueError:
        print("Something went wrong")
print(f"Thanks for your input, {name}!")

while True:
    try:
        num_str = input("Enter any number: ")
        if not num_str.isdigit():
            print ("I want the number in number format, not word format.")
            continue
        break
    except ValueError:
        print("Something went wrong")
print(f"Thanks for your input, {name}!")

n = int(num_str)

even_counter = 0
odd_counter = 0
total = 0

for i in range (1, n+1, 1):

    if i % 2 == 0:
        even_counter = even_counter + 1
    else:
        odd_counter = odd_counter + 1

    total = i + total

    print(f"""
        Iteration {i} of {n}
        Even numbers: {even_counter}
        Odd numbers: {odd_counter}
        Total: {total}
    """)        

# PRIME NUMBER CHALLENGE
print("PRIME NUMBER CHALLENGE")
while True:
    number_str = input("Enter any integer: ")
    if not number_str.isdigit():
        print ("I want the integer in number format, not word format")
        continue
    break
print (f"Thanks for your input, {name}!")

number = int(number_str)

prime_counter = 0

for number in range (1, number + 1, 1):
    if number == 1:
        continue

    divisor_found = False

    for i in range (2, number, 1):
        
        if number % i == 0:
            divisor_found = True
            break

    if divisor_found == False:
        prime_counter = prime_counter + 1

print(f"Prime numbers: {prime_counter}")    

