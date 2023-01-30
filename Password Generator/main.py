import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_letters = letters.lower()
digits = "1234567890"

symbols = "!@#$%^&*()+_|\\?/.,;' "

# Boolean values for each of the components

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += letters
if lower:
    all += lower_letters
if nums:
    all += digits
if syms:
    all += symbols
    
    
# Now i go ahead and specify the password length as well as the number of passwords i want the generator to generate


length = 10
amount = 10

# Here is the actual generator. I used for-loop.

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)