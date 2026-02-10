user_input = input("Enter a number for the multiplication table: ")
if user_input.isdigit():
    number = int(user_input)
    for i in range(1, 11):
        result = number * i
        print(f"{number} X {i} = {result:3}")