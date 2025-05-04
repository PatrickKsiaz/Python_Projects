#Mathematical Operations
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 4)
print(5 / 3)
print(5 // 3)
print(2**2)
print(2**3)


#PEMDAS --> Parentheses, Exponents, Multiplication and Division, Addition and Subtraction
# () 
# **
# * / 
# + OR -

# What is the output of this code??
print(3 * 3 + 3 / 3 - 3)

# Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#Number Manipulation
bmi = 84 / (1.65 ** 2)
print(bmi)

print(int(bmi))
print(round(bmi))

####################
score = 0
height = 1.8
is_winning = True

# User scores a point 
score -= 1 
print(score)

# f-stringss
#print("Your score is" + str(score))

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")


# Control Flow and Logical Operators


# if, elif, else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Modulo Operator
# % --> Modulo operator

#Even number 12 % 2 == 0 
#Odd number 13 % 2 == 1

number_to_check - input(int("What is your number do you want to check? "))

#print(number_to_check % 2)
if number_to_check % 2 == 0:
    print("Even")
else:
    (print("Odd"))

#Nested if statements and elif statemets

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age  = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")







