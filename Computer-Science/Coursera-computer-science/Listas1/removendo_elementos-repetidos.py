def remove_repetidos(lista):
    lista2 = []
    for item in lista:
        if item not in lista2:
            lista2.append(item)
    return sorted(lista2)

#lista3 = [2, 4, 2, 2, 3, 3, 1]

#print(remove_repetidos(lista3))