user_input = input("Gimme a number: ")

try:
    num = float(user_input)
except ValueError:
    print("Invalid input")
else:
    if num.is_integer():
        print("The number is an integer")
    else:
        print("The number is a decimal")
