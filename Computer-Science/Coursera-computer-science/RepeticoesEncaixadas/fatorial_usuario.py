def factorial(num):
    if num < 0:
        return "does not exist because is negative."

    elif num == 0:
        return 1

    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact

check_num = True
x = 5
while(check_num):
    try:
        while(x > 0):
            user_input = int(input("Type the numbers for see the factorial: "))
            int(user_input)
            print(factorial(user_input))
            x -= 1
            check_num = False
    except ValueError:
        check_num = True


