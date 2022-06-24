def soma_hipotenusas(n):
    arr = []
    while n > 0:
        for x in range(1, n):
           for y in range(1, n):
              if n ** 2 == x ** 2 + y ** 2:
                  arr.append(n)

        n = n - 1
    arr = remove_items_equal(arr)
    return sum(arr)

def remove_items_equal(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return l



#print(soma_hipotenusas(25))


