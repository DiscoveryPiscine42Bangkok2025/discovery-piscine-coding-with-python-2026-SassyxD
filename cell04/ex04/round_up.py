import math

user_input = input("Enter a number: ")

print(int(float(user_input)) + (1 if float(user_input) % 1 > 0 else 0))

# using math.ceil
# print(math.ceil(float(user_input)))