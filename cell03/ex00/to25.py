user_input = input("Enter a number less than 25 ")

if user_input.isdigit():
    number = int(user_input)
    if number < 25:
        for i in range(number, 26):
            print("Inside the loop, my variable is", i)
    else:
        print("Error")