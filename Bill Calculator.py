print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_cost = bill + (bill*tip/100)
cost_per_person = (total_cost / people)
rounded= round(cost_per_person, 6)

print(f"price per person: ${rounded}")