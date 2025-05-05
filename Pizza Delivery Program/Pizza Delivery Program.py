#Desciription: Based on the user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for thier order and tell them how much they have to pay.
# Small pizzza (S): 15$
# Medium pizza (M): 20$
# Large pizza (L): 25$
# Add pepperoni for small pizza(Y or N): 2$


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheesse = input("Do you want extra cheese? Y or N? ")

#todo: work out how much they need to pay based on their size choice
if size == "S":
    bill = 15
elif size == "M":
#todo: work out how much to add to their bill based on their pepperoni choice
    bill = 20
elif size == "L":
    bill = 25
#todo: work out their final amount basen on whether if they want extra cheese or not
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheesse == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
#
