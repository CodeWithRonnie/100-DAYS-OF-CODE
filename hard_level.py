import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [] # this is an empty list that will contain our random characters

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_numbers): # so same as easy level, characters will equal to the number the of the user input 
    password_list.append(random.choice(numbers)) # now to that list we append(add) the random choice of numbers
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

 
random.shuffle(password_list) # this will give us a shuffled list of all random selected characters from lists above
print(password_list)

password = "" # the we go back to giving password variable an empty string

for char in password_list: # for every character that is in the password_list
    password += char # add that character to the empty password string
    
print(password)