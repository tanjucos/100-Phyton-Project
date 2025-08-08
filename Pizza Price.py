print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

#Size of the Pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed unknown character please pick between s,m,l")

#Pepperoni addition
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#Extra Cheese
if extra_cheese == "Y":
    bill += 1

print(f"Final Cost ${bill}.")
