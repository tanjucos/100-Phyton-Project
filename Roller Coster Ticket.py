print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# Define the Variable that you want to have as an iterated outcome
bill = 0

#Check the indentation - if & else is dictating the main structure
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    #After passing the first if conditions, we create the different pricing categories
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    #elif statement allows as much as condition between if and else statements
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be OK. Have a ride with us! ")
    #else always ends with: since it represents the inverted list, alternatives, solutions, outcomes.
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
    #print statements are always in the same line of code be careful about it.