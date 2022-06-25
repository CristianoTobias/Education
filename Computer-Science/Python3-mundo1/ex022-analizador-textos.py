nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print(f"Seu nome em maiusculas é {nome.upper()}")
print(f"Seu nome em minusculas é {nome.lower()}")
print(f'Seu nome tem {len("".join(nome.split()))} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')


