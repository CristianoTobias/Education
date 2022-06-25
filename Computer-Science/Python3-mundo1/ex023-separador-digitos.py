num = int(input("Digite um número: "))
num = str(num)
num1 = num[::-1]
print(f"Analisando o numero {num}...")
print(f"Unidades: {num1[0]}")
print(f"Dezenas: {num1[1]}")
print(f"Centenas: {num1[2]}")
print(f"Milhar: {num1[3]}")