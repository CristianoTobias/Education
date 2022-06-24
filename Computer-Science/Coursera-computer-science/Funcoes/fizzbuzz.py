def fizzbuzz(x):
    if(x % 3 == 0 and x % 5 == 0):
        return "FizzBuzz"
    elif(x % 3 == 0 and not(x % 5 == 0)):
        return "Fizz"
    elif (not(x % 3 == 0) and x % 5 == 0):
        return "Buzz"
    else:
        return x
#print(fizzbuzz(15))