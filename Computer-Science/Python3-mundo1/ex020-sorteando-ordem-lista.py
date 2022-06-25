import random
from random import shuffle
aluno1 = input("Primerio aluno: ")
aluno2 = input("Primerio aluno: ")
aluno3 = input("Primerio aluno: ")
aluno4 = input("Primerio aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
lista2 = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
shuffle(lista)
print(f"O aluno escolhido foi {lista}")
print(f"O aluno escolhido foi {lista2}")




