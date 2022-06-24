def maior_primo(x):
    count = x - 1
    while count > 1:
        if x % count == 0:
            x -= 1
            count = x - 1
        else:
            count -= 1
    return x


#print(maior_primo(5))
