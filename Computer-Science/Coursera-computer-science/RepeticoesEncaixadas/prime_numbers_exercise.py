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
def n_primos(x):
    count = 0
    while x > 1:
        if is_prime(x):
            count = count + 1
        x = x - 1
    return count


#print(n_primos(2))