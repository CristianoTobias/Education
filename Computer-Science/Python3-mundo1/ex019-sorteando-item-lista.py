from random import randint, choice
aluno1 = input("Primerio aluno: ")
aluno2 = input("Primerio aluno: ")
aluno3 = input("Primerio aluno: ")
aluno4 = input("Primerio aluno: ")
lista = [aluno4, aluno3, aluno2, aluno1]
number = randint(0, 3)
print(f"O aluno escohido é {lista[number]}!")
print(print(f"O aluno escohido é {choice(lista)}!"))
