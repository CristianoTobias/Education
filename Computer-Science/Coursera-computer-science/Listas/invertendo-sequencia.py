lista = []
while(True):
    number = int(input("Digite um numero: "))
    if(number != 0):
        lista.append(number)
    else:
        break
for item in lista[::-1]:
    print(item)



