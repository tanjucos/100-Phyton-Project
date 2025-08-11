import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Level
password = ""

#4 digits from letters list by nr_letters
sel_letters = random.sample(letters, nr_letters)
print("Random Letters:", sel_letters)
#2 symbols from symbols lists by nr_symbols
sel_symbols = random.sample(symbols, nr_symbols)
print("Random Symbols:", sel_symbols)
#3 bznbers from numbers lists by nr_numbers
sel_numbers = random.sample(numbers, nr_numbers)
print("Random Numbers:", sel_numbers)

#Combining the lists = password
password = sel_letters + sel_symbols + sel_numbers
print(password)

# Easy Level
password = ""

#  nr_letters 4 - longer way to write
#for char in range (1, nr_letters +1):
    # 1- 4
    #random_char = random.choice(letters)
   # password = password + random_char
   # print(password)

#  nr_letters 4 - Shorter way to write
#for char in range(0, nr_letters):
#    password += random.choice(letters)

#for char in range(0, nr_symbols):
#    password += random.choice(symbols)

#for char in range(0, nr_numbers):
#    password += random.choice(numbers)

#print(password)


#  nr_letters 4 - Shorter way to write
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

# now we are done with the list [] we will write it as a string
password = ""
for char in password_list:
    password += char
print(f"Your new passowrd is. {password}")