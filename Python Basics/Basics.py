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
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("Please pay $12")
        bill = 12
    wants_photo = input("Do you want to have a photo take? Type y for Yest and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3 #15
        print(f"Your final bill is {bill}")
    else:
        print("Your photo is free.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Logical Operators






#Python Lists 


import  random
import my_module

random_integer = random.randint(a:1, b:10)
print(random_integer)

print(my_module.my_favourite_number)

random_number_0_to_1_ = random.random

#random.float - random.uniform(a:1, b:10)
print(random_float)

# random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# Radomisation and Pytho Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin"]

print(len(states_of_america))

print(states_of_america[0])
print(states_of_america[1])

states_of_america.extend = ["New York", "New Jersey", "New Hampshire"]
print(states_of_america)

# Who pay the bill ? 

friends = ["Angela", "James", "Lily", "Jack"]

#1 Option
print(random.choice(friends))

#2nd Option
random_index = random.randint (a:0, b:4)
print(friends[random_index])

dirty_dozen = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Peach", "Plum", "Cherry", "Strawberry", "Blueberry", "Raspberry"]

fruits = ["Strawberry", "Blueberry", "Raspberry", "Blackberry", "Watermelon"]
vegetables = ["Carrots", "Broccoli", "Cauliflower", "Brussels Sprouts", "Asparagus"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Loops 

fruits = ["Strawberry", "Blueberry", "Raspberry", "Blackberry", "Watermelon"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)

print(fruits)











