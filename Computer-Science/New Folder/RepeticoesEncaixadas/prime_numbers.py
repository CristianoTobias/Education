
def is_prime(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True
n = int(input("Type a integer number: "))
while n > 0:
    if is_prime(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")
    n = int(input("Type a integer number: "))


